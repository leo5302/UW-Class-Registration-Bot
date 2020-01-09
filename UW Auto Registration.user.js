// ==UserScript==
// @name         UW Auto Registration
// @namespace    https://github.com/leo5302
// @version      1.0
// @description  Your account will get locked if you abuse this.
// @author       leo5302
// @match        https://sdb.admin.uw.edu/students/uwnetid/register.asp
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function register() {
        await sleep(500);
        document.getElementById("regform")[85].click();
        await sleep(500);
    }

    register();
})();
