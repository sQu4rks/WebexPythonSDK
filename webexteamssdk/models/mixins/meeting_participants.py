# -*- coding: utf-8 -*-
"""Webex MeetingParticipants data model.

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



class MeetingParticipantBasicPropertiesMixin(object):
    """MeetingParticipant basic properties."""
    
    @property
    def id(self):
        """The participant id to uniquely identify the meeting and the participant."""
        return self._json_data.get("id")
    
    @property
    def orgId(self):
        """The id to identify the organization."""
        return self._json_data.get("orgId")
    
    @property
    def host(self):
        """Whether or not the participant is the host of the meeting."""
        return self._json_data.get("host")
    
    @property
    def coHost(self):
        """Whether or not the participant has host privilege in the meeting."""
        return self._json_data.get("coHost")
    
    @property
    def spaceModerator(self):
        """Whether or not the participant is the team space moderator. This field returns only if the meeting is associated with a Webex space."""
        return self._json_data.get("spaceModerator")
    
    @property
    def email(self):
        """The email address of the participant."""
        return self._json_data.get("email")
    
    @property
    def displayName(self):
        """The name of the participant."""
        return self._json_data.get("displayName")
    
    @property
    def invitee(self):
        """Whether or not the participant is invited to the meeting."""
        return self._json_data.get("invitee")
    
    @property
    def muted(self):
        """Whether or not the participant's audio is muted."""
        return self._json_data.get("muted")
    
    @property
    def video(self):
        """The status of the participant's video. (Values: on, off)"""
        return self._json_data.get("video")
    
    @property
    def state(self):
        """The status of the participant in the meeting. (Values: lobby, end, joined)"""
        return self._json_data.get("state")
    
    @property
    def joinedTime(self):
        """The time the participant joined the meeting. If the field is non-existent or shows 1970-01-01T00:00:00.000Z the meeting may be still ongoing and the joinedTime will be filled in after the meeting ended."""
        return self._json_data.get("joinedTime")
    
    @property
    def leftTime(self):
        """The time the participant left the meeting. If the field is non-existent or shows 1970-01-01T00:00:00.000Z the meeting may be still ongoing and the leftTime will be filled in after the meeting ended."""
        return self._json_data.get("leftTime")
    
    @property
    def siteUrl(self):
        """The site URL."""
        return self._json_data.get("siteUrl")
    
    @property
    def meetingId(self):
        """A unique identifier for the meeting which the participant belongs to."""
        return self._json_data.get("meetingId")
    
    @property
    def hostEmail(self):
        """The email address of the host."""
        return self._json_data.get("hostEmail")
    
    @property
    def devices(self):
        """List of devices for this participant joined in the call."""
        return self._json_data.get("devices")
    
    @property
    def sourceId(self):
        """The source ID of the participant."""
        return self._json_data.get("sourceId")
    