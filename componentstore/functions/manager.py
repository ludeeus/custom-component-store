"""File manager."""
import os
import requests
from componentstore.const import PATH
from componentstore.functions.data import get_data


async def install_component(component):
    """Install component"""
    comp_data = await get_data()
    embedded = comp_data[component].get('embedded')
    if embedded:
        localpath = PATH + comp_data[component]['embedded_path']
        remotepath = comp_data[component]['embedded_path_remote']

        if '.' in component:
            if not os.path.exists(
                    PATH + '/custom_components/' + component.split('.')[1]):
                os.makedirs(
                    PATH + '/custom_components/' + component.split('.')[1])

        if '__init__.py' in comp_data[component]['embedded_path']:
            if not os.path.exists(PATH + '/custom_components/' + component):
                os.makedirs(PATH + '/custom_components/' + component)

        with open(localpath, 'wb') as file:
            file.write(requests.get(remotepath).content)
        file.close()


async def uninstall_component(component):
    """Uninstall component"""
    comp_data = await get_data()
    embedded = comp_data[component].get('embedded')
    if embedded:
        path = PATH + comp_data[component]['embedded_path']
    else:
        path = PATH + comp_data[component]['local_location']
    os.remove(path)


async def migrate_component(component):
    """Migrate component"""
    comp_data = await get_data()
    old_path = PATH + comp_data[component]['local_location']
    new_path = PATH + comp_data[component]['embedded_path']
    print('From', old_path, 'to', new_path)
    if '.' in component:
        if not os.path.exists(
                PATH + '/custom_components/' + component.split('.')[1]):
            os.makedirs(
                PATH + '/custom_components/' + component.split('.')[1])
    os.rename(old_path, new_path)
