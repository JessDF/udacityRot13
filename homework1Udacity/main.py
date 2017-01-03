#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class Rot13(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('form.html')
		self.response.write(template.render())

	def post(self):
		rot13 = ''
		text = self.request.get('text')
		if text:
			rot13 = text.encode('rot13')
		values = {'text': rot13}
		template = jinja_environment.get_template('form.html')
		self.response.write(template.render(values))

app = webapp2.WSGIApplication([('/', Rot13)], debug=True)
