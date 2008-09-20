# Patchwork - automated patch tracking system
# Copyright (C) 2008 Jeremy Kerr <jk@ozlabs.org>
#
# This file is part of the Patchwork package.
#
# Patchwork is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Patchwork is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Patchwork; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import os
from patchwork.models import Project
try:
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
except ImportError:
    # Python 2.4 compatibility
    from email.MIMEText import MIMEText
    from email.MIMEMultipart import MIMEMultipart

# helper functions for tests
_test_mail_dir  = 'patchwork/tests/mail'
_test_patch_dir = 'patchwork/tests/patches'

class defaults(object):
    project = Project(linkname = 'test-project', name = 'Test Project')

    patch_author = 'Patch Author <patch-author@example.com>'

    comment_author = 'Comment Author <comment-author@example.com>'

    sender = 'Test Author <test-author@example.com>'

    subject = 'Test Subject'

    patch_name = 'Test Patch'


def read_patch(filename):
    return file(os.path.join(_test_patch_dir, filename)).read()

def create_email(content, subject = None, sender = None, multipart = False,
        project = None):
    if subject is None:
        subject = defaults.subject
    if sender is None:
        sender = defaults.sender
    if project is None:
        project = defaults.project

    if multipart:
        msg = MIMEMultipart()
        body = MIMEText(content, _subtype = 'plain')
        msg.attach(body)
    else:
        msg = MIMEText(content)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['List-Id'] = project.linkname

    return msg
