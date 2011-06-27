#  ============================================================================
#
#  Copyright (C) 2007-2011 Conceptive Engineering bvba. All rights reserved.
#  www.conceptive.be / project-camelot@conceptive.be
#
#  This file is part of the Camelot Library.
#
#  This file may be used under the terms of the GNU General Public
#  License version 2.0 as published by the Free Software Foundation
#  and appearing in the file license.txt included in the packaging of
#  this file.  Please review this information to ensure GNU
#  General Public Licensing requirements will be met.
#
#  If you are unsure which license is appropriate for your use, please
#  visit www.python-camelot.com or contact project-camelot@conceptive.be
#
#  This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
#  WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#
#  For use of this library in commercial applications, please contact
#  project-camelot@conceptive.be
#
#  ============================================================================

"""Camelot specific subclasses of Exception
"""

class UserException(Exception):
    """
    Raise this exception to inform the user he did something wrong, without
    showing a stack trace or other internals.  Raising this exception won't
    log stack traces either, as the occurance of this exception is considered
    a non-event for the developer.
    """
    
    def __init__(self, title, text, icon=None, resolution=None, detail=None):
        """
        :param title: the title of the dialog box that informs the user
        :param text: the top text in the dialog
        :param resolution: what the user should do to solve the issue
        :param detail: a detailed description of what went wrong
        """
        super(UserException, self).__init__(text)
        self.title = title
        self.text = text
        self.icon = icon
        self.resolution = resolution
        self.detail = detail