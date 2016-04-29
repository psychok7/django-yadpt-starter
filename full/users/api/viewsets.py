# -*- coding: utf-8 -*-

import logging
import datetime
import uuid

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from django.contrib.auth.models import Group
from dorothy import router
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework.decorators import list_route
from rest_framework import viewsets, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authtools.forms import FriendlyPasswordResetForm

from .serializers import UserProfileSerializer, UserSerializer
from .authentication import NoAuthentication
from users.models import UserProfile

log = logging.getLogger('dorothy_console')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (NoAuthentication,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'email', 'name')

    def get_queryset(self):
        # https://github.com/tomchristie/django-rest-framework/issues/1067#issuecomment-197947538
        user = TokenAuthentication().authenticate(self.request)
        if user is not None:
            user = user[0]
            if user.is_superuser:
                return get_user_model().objects.all()
            else:
                return get_user_model().objects.filter(id=user.id)

        return get_user_model().objects.none()

    def create(self, request, *args, **kwargs):
        """

        Register User <b>STATUS OK</b>.
        ======================================

        Registers a user.

        <b>Details</b>

        <b>HEADERS :</b> CONTENT: application/json.

        <b>STATUS :</b> 201 CREATED.

        <b>RETURN :</b> Information about the new user.

        <b>AUTHENTICATION :</b> Not required

        <b>Body data POST Example</b>

        <pre><code>
        {
          "name": "test",
          "is_guest": false,
          "membership_type": "personal",
          "email": "test@ubiwhere.com",
          "password": "123qwe",
          "phone": "96XXXXX"
        }
        </code></pre>

        <b>Response Example</b>

        <pre><code>
        {
            "id": 26,
            "email": "test@ubiwhere.com",
            "name": "test",
            "api_token": "58118381f0759ac2e91546bdecd4ae0ccb35865c",
            "last_login": null
        }
        </code></pre>

        ---
        # Using YAML to do more things.
        # https://github.com/marcgibbons/django-rest-swagger/blob/0.2.1/docs/source/yaml.rst

        parameters:
            - id: id
              paramType: query
            - email: email
              paramType: query
            - name: name
              paramType: query

        responseMessages:
            - code: 400
              message: Whenever the submitted data contains errors

        """
        guest_email = None
        if 'POST' in request.method:
            if request.data.get('is_guest') is not None:
                if request.data['is_guest'] == True:
                    guest_email = request.data['email']
                    request.data['email'] = str(uuid.uuid4()) + '@dorothy.com'

            if request.data.get('membership_type') is None:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={'detail': 'membership_type is required'}
                )

            if request.data.get('phone'):
                request.data['user_profile'] = {
                    'phone': request.data['phone']
                }
        # Make sure userprofile is created first.
        response = super(UserViewSet, self).create(request, *args, **kwargs)
        user = get_object_or_404(get_user_model(), pk=response.data['id'])

        if request.data.get('is_guest') is not None:
            if request.data['is_guest'] == True:
                user.userprofile.is_guest = request.data['is_guest']
                user.userprofile.guest_email = guest_email
                user.userprofile.save()

        # Guest user don't need permissions
        if not user.userprofile.is_guest:
            # Add user to group so he can have full access.
            group = get_object_or_404(Group, name=request.data['membership_type'])
            user.groups.add(group)
            log.info('Added {user} to group {group}'.format(**locals()))

        return response

    @list_route(
        methods=['post'], permission_classes=[AllowAny],
        authentication_classes=[NoAuthentication]
    )
    def login(self, request):
        """

        Login User <b>STATUS OK</b>.
        =======================================================

        Logs in the user specified by {email} and {password}.

        <b>Details</b>

        <b>METHODS :</b> POST

        <b>HEADERS :</b> CONTENT: application/json.

        <b>RETURN :</b> The user's API key for accessing the Dorothy API.

        <b>STATUS :</b> 200 OK.

        <b>Parameters (not automatically generated):</b>

        <pre>
        password : Represents the user's password.
        </pre>

        <b>Body data Example for Email/Password Login</b>
        <pre><code>
        {
            "email": "test@example.com",
            "password": "safe#passw0rd!"
        }
        </code></pre>

        <b>Custom Response (please ignore the auto generated Response Class Model)</b>
        <pre><code>
            {
                "email": "joana@ubiwhere.com",
                "id": 25,
                "api_token": "9613153e624b5b0113d695847759daffac833eca",
                "phone": "962823e",
                "name": "joana"
            }
        </code></pre>

        ---
        # Using YAML to do more things.
        # https://github.com/marcgibbons/django-rest-swagger/blob/0.2.1/docs/source/yaml.rst

        parameters_strategy: merge
        omit_parameters:
            - form

        responseMessages:
            - code: 401
              message: UNAUTHORIZED, something wrong with user credentials
            - code: 405
              message: Whenever trying to access the endpoint using a method other than POST

        """
        def email_password_login(email, password):
            user = authenticate(email=email, password=password)
            if user:
                try:
                    user_profile = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                else:
                    serializer = UserProfileSerializer(user_profile)
                    user.last_login = datetime.datetime.now()
                    user.save()
                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            'id': user.id,
                            'name': user.name, 'email': user.email,
                            'api_token': serializer.data['api_token'],
                            'token_type': 'Token',
                            'phone': serializer.data['phone']
                        }
                    )
            else:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        'success': False,
                        'detail': (
                            'UNAUTHORIZED. Are the user credentials correct?'
                        )
                    }
                )

        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            return email_password_login(email=email, password=password)

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={'detail': 'Email and Password are required'}
        )

    @list_route(
        methods=['post'], permission_classes=[AllowAny],
        authentication_classes=[NoAuthentication]
    )
    def recover_password(self, request):
        """

        Recover User Password <b>STATUS OK</b>.
        =======================================================

        Sends an email to a user with instructions on how to recover the password.

        <b>Details</b>

        <b>METHODS :</b> POST

        <b>HEADERS :</b> CONTENT: application/json.

        <b>RETURN :</b> Nothing.

        <b>STATUS :</b> 200 OK.

        <b>Parameters (not automatically generated):</b>

        <pre>
        email: The user's email address (Required)
        </pre>

        <b>Body data Example</b>

        <pre><code>
            {
                "email": "mail@example.com"
            }
        </code></pre>

        ---
        # Using YAML to do more things.
        # https://github.com/marcgibbons/django-rest-swagger/blob/0.2.1/docs/source/yaml.rst

        type:
          email (The user's email address):
            required: true
            type: string

        parameters_strategy: merge
        omit_parameters:
            - form

        responseMessages:
            - code: 400
              message: Whenever the submitted data contains errors

        """
        if request.data.get('email'):
            # Lets be smart and reuse django-authtools password recovery system
            form = FriendlyPasswordResetForm({'email': request.data.get('email')})
            if form.is_valid():
                form.save()
                return Response(status=200, data={'success': True})
        return Response(
            status=400,
            data={
                'detail': 'Something went wrong, make sure the email is set and'
                          ' it exists',
                'success': False
            }
        )

router.register(r'user', UserViewSet, base_name="user")
