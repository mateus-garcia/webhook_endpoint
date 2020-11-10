import os
from glob import glob

import dash_core_components as dcc
import dash_html_components as html


def getSubfolders(path):
    folders = glob(path + '\\*\\')
    subFolders = []
    for folder in folders:
        subFolders.append(folder.split('\\')[-2])
    try:
        subFolders.remove('__pycache__')
    except:
        pass
    return subFolders


def headers(i, string, link):
    if i == 1:
        return html.H1(dcc.Link(string, href=link))
    elif i == 2:
        return html.H2(dcc.Link(string, href=link))
    elif i == 3:
        return html.H3(dcc.Link(string, href=link))
    elif i == 4:
        return html.H4(dcc.Link(string, href=link))
    elif i == 5:
        return html.H5(dcc.Link(string, href=link))
    elif i == 6:
        return html.H6(dcc.Link(string, href=link))
    else:
        return html.H6(dcc.Link(string, href=link))


def sideBar(pathname):
    mainPath = os.path.dirname(__file__)
    structure = pathname.split('/')
    print('______________________')
    print(mainPath)
    defaultMenu = {'app1': 'App 1', 'app2': 'App 2'}
    menu = []
    aux = []
    for item in defaultMenu.keys():
        menu.append(html.H2(dcc.Link(defaultMenu[item], href='/apps/' + item)))
        aux.append(item)
        if len(structure) > 2:
            if item == structure[2]:
                relativePath = '\\apps'
                for i in range(2, len(structure)):

                    relativePath = relativePath + "\\" + structure[i]
                    foldList = getSubfolders(mainPath + '\\' + relativePath)
                    ind = aux.index(structure[i])
                    print(aux)
                    print(ind)
                    for j in range(len(foldList)):
                        link = relativePath + '\\' + foldList[j]
                        link = link.replace('\\', '/')

                        menu.insert(ind + 1 + j, headers(i + 2, foldList[j], link))
                        aux.insert(ind + 1 + j, foldList[j])

        menu.append(html.Br())
        aux.append(' ')
    # print(aux)
    print(aux)
    print(menu)
    return menu
