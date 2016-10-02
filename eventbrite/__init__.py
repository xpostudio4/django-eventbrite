""""
 Copyright (c) Copyright 2010 Fwix, Inc. Josh Toft <josh@fwix.com>

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.

 Eventbrite api
 Modified by Michael Clemmons for Caktus Consulting Group
"""

import hashlib
import urllib
import httplib2
import simplejson

from django.conf import settings

__all__ = ['APIError', 'API']

class APIError(Exception):
    pass

class API:
    def __init__(self, server='www.eventbrite.com', cache=None):
        """Create a new Eventbrite API client instance.
        If you don't have an application key, you can request one:
        http://www.eventbrite.com/api/key/"""
        self.app_key = settings.EVENTBRITE_APP_KEY
        self.server = server
        self.http = httplib2.Http(cache)
        if settings.EVENTBRITE_USER_KEY:
            self.user_key = settings.EVENTBRITE_USER_KEY
            self.user = settings.EVENTBRITE_USER

    def call(self, method, **args):
        "Call the Eventbrite API's METHOD with ARGS."
        # Build up the request
        args['app_key'] = self.app_key
        if hasattr(self, 'user_key'):
            args['user'] = self.user
            args['user_key'] = self.user_key
        args = urllib.parse.urlencode(args)
        url = "https://%s/json/%s?%s" % (self.server, method, args)

        # Make the request
        response, content = self.http.request(url, "GET")

        # Handle the response
        status = int(response['status'])
        if status == 200:
            try:
                return simplejson.loads(content)
            except ValueError:
                raise APIError("Unable to parse API response!")
        elif status == 404:
            raise APIError("Method not found: %s" % method)
        else:
            raise APIError("Non-200 HTTP response status: %s" % response['status'])

