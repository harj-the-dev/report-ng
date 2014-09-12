# Wasar
# Copyright (c) 2014 Marcin Woloszyn (@hvqzao)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


def request_tune(content):
    return content.strip()

def response_tune(content):
    blank = content.find('\n\n')
    if blank == -1:
        return content.strip()
    else:
        return (content[:blank+2]+'\n'.join(content[blank+2:].split('\n')[:4])+'\n[...]').strip()

def http_param_truncate(param, search=['__VIEWSTATE', 'javax.faces.ViewState'], maxlen=160, replacement='[...]'):
    if not isinstance(search,list):
        search = [search]
    if not filter(lambda x: x+'=' in param, search):
        return param
    for subject in search:
        out = []
        for keyval in map(lambda x: x.split('='), param.split('&')):
            if len(keyval) > 1 and keyval[0] == subject and len(keyval[1]) > maxlen:
                bound = maxlen/2-len(replacement)
                if bound < 1:
                    bound = 5
                keyval[1] = keyval[1][:bound]+replacement+keyval[1][-bound:]
            out += ['='.join(keyval)]
        param = '&'.join(out)
        del out
    #print param
    #import sys; sys.exit()
    return param
    
if __name__ == '__main__':
    pass

    #print request_tune(open('../examples/tmp/b-request.txt').read())
    print response_tune(open('../examples/tmp/b-response.txt').read())