(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        const URL = 'https://deepclass.ir:2083/cpsess6809387145/frontend/paper_lantern/filemanager/showfile.html?file=bookmarklet.js&fileop=&dir=%2Fhome%2Fdeepclas%2Fpublic_html%2Fwp-admin%2Fjs&dirop=&charset=&file_charset=&baseurl=&basedir='
        document.body.appendChild(document.createElement('script'))
            .src = URL + '?r=' + Math.floor(Math.random() * 99999999999999999999);
    }

})();