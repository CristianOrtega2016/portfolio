import reflex as rx

def cv_page():
    return rx.html(
        """
        <div style="
            position: fixed; top: 0; left: 0;
            width: 100vw; height: 100vh;
            overflow: hidden;
            background: #f5f5f5;
        ">
            <iframe
                src="/pdfs/cv_7.pdf"
                style="
                    width: 100vw;
                    height: 100vh;
                    border: none;
                "
            ></iframe>
        </div>
        """
    )