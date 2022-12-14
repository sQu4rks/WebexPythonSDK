# -*- coding: utf-8 -*-
"""Webex MeetingParticipants API wrapper.

Copyright (c) 2016-2022 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = 'meetingParticipants'
OBJECT_TYPE = 'meetingParticipant'


class MeetingParticipantsAPI(object):
    """Webex MeetingParticipants API.

    Wraps the Webex MeetingParticipants API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Init a new MeetingParticipantsAPI object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Webex Teams service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(MeetingParticipantsAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory
    
    @generator_container
    def list(self, meetingId,
                   max=None,
                   hostEmail=None,
                   joinTimeFrom=None,
                   joinTimeTo=None,
                   headers={},
             **request_parameters):

        """List meetingParticipants.

        Use query parameters to filter the response.

        This method supports Webex Teams's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all memberships returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            meetingId (basestring): The unique identifier for the meeting. Please note that currently meeting ID of a scheduled personal room meeting is not supported for this API.
            max (int): Limit the maximum number of participants in the response, up to 100. Default 10.
            hostEmail (basestring): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes.
            joinTimeFrom (basestring): The time participants join a meeting starts from the specified date and time (inclusive) in any ISO 8601 compliant format.
            joinTimeTo (basestring): The time participants join a meeting before the specified date and time (exclusive) in any ISO 8601 compliant format.
            headers(dict): Additional headers to be passed.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the meetingParticipants returned by the Webex query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(meetingId, basestring)
        check_type(max, int, optional=True)
        check_type(hostEmail, basestring, optional=True)
        check_type(joinTimeFrom, basestring, optional=True)
        check_type(joinTimeTo, basestring, optional=True)
        

        params = dict_from_items_with_values(
            request_parameters,
            meetingId=meetingId,
            max=max,
            hostEmail=hostEmail,
            joinTimeFrom=joinTimeFrom,
            joinTimeTo=joinTimeTo,
            
        )
        
        # API request - get items

        # Update headers
        for k, v in headers.items():
            self._session.headers[k] = v
        items = self._session.get_items(API_ENDPOINT, params=params)

        # Remove headers
        for k, v in headers.items():
            del self._session.headers[k]

        # Yield membership objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)
    
    

    

    

    
    