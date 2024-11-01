import sys
import xbmc
import xbmcaddon
import urllib.parse

ADDON = xbmcaddon.Addon('script.module.json-cec')
ADDON_NAME = ADDON.getAddonInfo('name')

actions = {
    'activate': 'CECActivateSource',
    'toggle': 'CECToggleState',
    'standby': 'CECStandby',
}

def log(text):
    message = f'{ADDON_NAME}: {text}'
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)
    return

def run():
    try:
        params = urllib.parse.parse_qs('&'.join(sys.argv[1:]))
        command = params['command'][0]
    except (IndexError, KeyError) as error:
        log('Missing "command" parameter, exiting')
        return

    try:
        action = actions[command]
    except KeyError as error:
        log(f'Invalid "command" value: {command}, exiting')
        return

    xbmc.executebuiltin(action)
    return
