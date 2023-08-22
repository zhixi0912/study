let step = 0;
export function corrugation(can: any) {
    
    const canvas = can
    let ctx = canvas.getContext("2d");//设置2D渲染区域
    
    let boHeight = 300/10;
    let posHeight = 300/1.1;
    let colors = ['rgba(216, 242, 252, 0.9)', 'rgba(216, 242, 252,  0.7)', 'rgba(216, 242, 252,  0.5)']
    ctx.lineWidth = 5;//设置线的宽度
    let widths = canvas.parentNode.offsetWidth
    canvas.width = widths
    canvas.height = 300
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 清空画布
    step += 1; // 角度
    // 遍历colors数组，进行绘制
    colors.forEach((item, index) => {
        ctx.fillStyle = item; // 画笔的颜色
        let angle = (step + index * 50) * Math.PI / 180; // 相差的角度
        let deltaHeight = Math.sin(angle) * boHeight; // 线条左边的起点
        let deltaHeightRight = Math.cos(angle) * boHeight; //线条右边的终点
        ctx.beginPath();
        ctx.moveTo(0, posHeight + deltaHeight);
        ctx.bezierCurveTo(canvas.width / 2, posHeight + deltaHeight - boHeight, canvas.width / 2, posHeight +
            deltaHeightRight - boHeight, canvas.width, posHeight + deltaHeightRight); // 绘制贝塞尔曲线
        ctx.lineTo(canvas.width, canvas.height); // 防止右侧出现空隙
        ctx.lineTo(0, canvas.height); // 防止左侧出现空隙
        ctx.closePath();
        ctx.fill();
    })
//    corrugation(canvas)
}