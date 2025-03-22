var googleAuth = (function() {
    function installClient() {
        var apiUrl = 'https://apis.google.com/js/api.js'
        return new Promise((resolve) => {
            var script = document.createElement('script')
            script.src = apiUrl
            script.onreadystatechange = script.onload = function() {
                if(!script.readyState || /loaded|complete/.test(script.readyState)) {
                    setTimeout(function() {
                        resolve()
                    }, 500)
                }
            }
            document.getElementsByTagName('head')[0].appendChild(script)
        })
    }

    function initClient(options) {
        return new Promise((resolve, reject) => {
            window.gapi.load('auth2', () => {
                window.gapi.auth2.init(options)
                .then(() => {
                    resolve(window.gapi)
                })
                .catch((error) => {
                    reject(error)
                })
            })
        })
    }

    function Auth () {
        if(!(this instanceof Auth)) {
            return new Auth()
        }

        this.GoogleAuth = null
        this.isAuthorized = false
        this.isInit = false
        this.prompt = null


        this.load = (config, prompt) => {
            installClient()
            .then(() => {
                return initClient(config)
            })

            .then((gapi) => {
                this.GoogleAuth = gapi.auth2.getAuthInstance()
                this.prompt = prompt
                this.isInit = true
                this.isAuthorized = this.GoogleAuth.isSignedIn.get()
            })
        }

        this.signIn = (successCallback, errorCallback) => {
            return new Promise((resolve, reject) => {
                if (!this.GoogleAuth) {
                    if (typeof errorCallback === 'function') errorCallback(false)
                    reject(false)
                    return
                }
                this.GoogleAuth.signIn()
                .then(googleUser => {
                      if (typeof successCallback === 'function') successCallback(googleUser)
                    this.isAuthorized = this.GoogleAuth.isSignedIn.get()
                    resolve(googleUser)
                })
                .catch(error => {
                    if (typeof errorCallback === 'function') errorCallback(error)
                    reject(error)
                })
            })
        }

        this.getAuthCode = (successCallback, errorCallback) => {
            return new Promise((resolve, reject) => {
                if (!this.GoogleAuth) {
                    if (typeof errorCallback === 'function') errorCallback(false)
                    reject(false)
                    return
                }
                const options = {
                    prompt: this.prompt
                }
                this.GoogleAuth.grantOfflineAccess(options)
                .then(function(resp) {
                    if (typeof successCallback === 'function') successCallback(resp)
                    resolve(resp)
                })
                .catch(function(error) {
                    if (typeof errorCallback === 'function') errorCallback(error)
                    reject(error)
                })
            })
        }

        this.signOut = (successCallback, errorCallback) => {
            return new Promise((resolve, reject) => {
                if (!this.GoogleAuth) {
                    if (typeof errorCallback === 'function') errorCallback(false)
                    reject(false)
                    return
                }
                this.GoogleAuth.signOut()
                .then(() => {
                    if (typeof successCallback === 'function') successCallback(true)
                    this.isAuthorized = false
                    resolve(true)
                })
                .catch(error => {
                    if (typeof errorCallback === 'function') errorCallback(error)
                    reject(error)
                })
            })
        }
    }

    return new Auth()
})()

function installGoogleAuthPlugin(app, options) {
    let GoogleAuthConfig = null
    let GoogleAuthDefaultConfig = { scope: 'profile email', discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'] }
    let prompt = 'select_account'
    if (typeof options === 'object') {
        GoogleAuthConfig = Object.assign(GoogleAuthDefaultConfig, options)
        if (options.scope) GoogleAuthConfig.scope = options.scope
        if (options.prompt) prompt = options.prompt
        if (!options.clientId) {
            console.warn('clientId is required')
        }
    } else {
        console.warn('invalid option type. Object type accepted only')
    }

    app.config.globalProperties.$gAuth = googleAuth
    googleAuth.load(GoogleAuthConfig, prompt)
}

export default installGoogleAuthPlugin
