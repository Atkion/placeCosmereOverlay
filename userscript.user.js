// ==UserScript==
// @name         r/placeCosmere Logo Template (modified for Stardew Valley)
// @namespace    http://tampermonkey.net/
// @version      0.3
// @description  try to take over the canvas!
// @author       oralekin, exdeejay (xDJ_), modified for r/placeCosmere by Atkion
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
            document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
				(function () {
					
					const i = document.createElement("img");
					i.src = "https://github.com/Atkion/placeCosmereOverlay/raw/master/template.png";
					i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
					console.log(i);

                    return i;
				})());
        document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
				(function () {

					const i = document.createElement("img");
					i.src = "https://r-placetux.github.io/place_tux/tux_overlay.png";
					i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
					console.log(i);

                    return i;
				})())
       /* document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            const i = document.createElement("img");
            i.src = "https://github.com/Lopeh/onepiece-place/raw/main/onepiece_template.png";
            i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 2000px;";
            console.log(i);
            return i;
        })())
		 document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            const i = document.createElement("img");
            i.src = "https://github.com/Atkion/placeCosmereOverlay/raw/master/FantasyAlliance.png";
            i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 2000px;";
            console.log(i);
            return i;
        })())*/

 
    }, false);

}
