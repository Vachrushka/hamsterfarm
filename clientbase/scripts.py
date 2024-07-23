access_enter = ("if (location.hostname === 'hamsterkombatgame.io') {"
                "const original_indexOf = Array.prototype.indexOf;"
                "Array.prototype.indexOf = function (...args) {"
                "if (JSON.stringify(this) === JSON.stringify(['android', 'android_x', 'ios'])) {"
                "setTimeout(() => {Array.prototype.indexOf = original_indexOf;}, 0);"
                "return 0; }"
                "return original_indexOf.apply(this, args);};")
clicker = ("const buttonSelector = '.user-tap-button';"
           "const energySelector = '.user-tap-energy > p';"
           "let reachedZeroEnergy = false;"
           "let button;let attempts = 0;const maxAttempts = 100;"
           "function checkButtonAndEnergy() {attempts++;"
           "button = document.querySelector(buttonSelector);"
           "if (button || attempts >= maxAttempts) {"
           "if (button) {"
           "console.log('Button found');"
           "} else {console.log('Max attempts reached, stopping search');}"
           "clearInterval(searchInterval);"
           "tick();} else {"
           "console.log('Button not found yet, attempt:', attempts);}}"
           "function tick() {try {const energyElement = document.querySelector(energySelector);"
           "if (energyElement) {const energyStr = energyElement.innerText;"
           "const [currEnergy, maxEnergy] = energyStr.split('/').map(Number);if (!reachedZeroEnergy) {"
           "button.dispatchEvent(new PointerEvent('pointerup'));"
           "button.dispatchEvent(new PointerEvent('pointerup'));"
           "button.dispatchEvent(new PointerEvent('pointerup'));"
           "button.dispatchEvent(new PointerEvent('pointerup'));}"
           "if (currEnergy <= 10) {reachedZeroEnergy = true;}"
           "if (currEnergy >= maxEnergy - 10) {"
           "reachedZeroEnergy = false;}}} catch (e) {console.log(e);}setTimeout(tick, 100 * Math.random() + 50);}"
           "const searchInterval = setInterval(checkButtonAndEnergy, 500);")

end_script = '}'


def get_access_enter():
    return access_enter + end_script


def get_access_new_wind(new_tab):
    access_new_wind = access_enter + (f"if ({new_tab}) "
                                      "{oldSubstring = '=web&';newSubstring = '=android&';"
                                      "let newWebLink = web_link.replace(oldSubstring, newSubstring);"
                                      "if (confirm('Открыть хомяка в отдельном окне?')) {"
                                      "window.open(newWebLink);}}")
    return access_new_wind + end_script


def get_access_click():
    access_click = access_enter + clicker
    return access_click + end_script


def get_access_click_new_web(new_tab):
    access_click_new_web = get_access_new_wind(new_tab)[:-1] + clicker
    return access_click_new_web + end_script
