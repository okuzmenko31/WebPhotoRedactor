import img3Src from "../assets/2in.png"

export default function handlePopState() {
    function deleteAllCircles() {
        const circles = document.querySelectorAll('.blur-circle')
        circles.forEach(circle => {
            circle.remove()
        })
    }
    deleteAllCircles();

    function createCircles() {
        const app = document.getElementById("app");
        const body = document.body;
    
        const spacing = 1100;
    
        const appHeight = app.clientHeight;
        const numCircles = Math.max(1, Math.floor(appHeight / spacing - 1));
    
        for (let i = 0; i < numCircles; i++) {
            const img1 = document.createElement("img");
    
            img1.className = "blur-circle";
    
            if (i == 0) {
                img1.style.top = `250px`;
            } else {
                const marginTop = i * spacing;
                img1.style.top = `${marginTop}px`;
            }
    
            img1.src = img3Src;
    
            body.appendChild(img1);
        }
    }
    createCircles();
}