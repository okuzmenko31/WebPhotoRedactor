export const deleteAllCircles = () => {
    const circles = document.querySelectorAll('.blur-circle')
    circles.forEach(circle => {
        circle.remove()
    })
}