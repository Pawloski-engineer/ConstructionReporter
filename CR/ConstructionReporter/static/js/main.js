window.onload = () => {
  'use strict';

  if ('serviceWorker' in navigator) {
                    navigator.serviceWorker
                            .register('{{ url "sw.js" }}', { scope: '/' }).then(function(reg) {
                        // registration worked
                        console.log('Registration succeeded. Scope is ' + reg.scope);
                    }).catch(function(error) {
                        // registration failed
                        console.log('Registration failed with ' + error);
                    });
                }
  else {
  console.log('no service worker found')
  }

}
