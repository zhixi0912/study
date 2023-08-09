import {onUnmounted, ref} from 'vue';

export function useDefer(maxCount = 100) {
    const frameCount = ref(0);
    let rafId: any;
    function updateFrameCount() {
        rafId = requestAnimationFrame(()=>{
            frameCount.value++;
            if (frameCount.value >= maxCount) {
                return;
            }
            updateFrameCount();
        })
    }
    updateFrameCount();
    onUnmounted(()=>{
        requestAnimationFrame(rafId);
    })
    return function defer(n: any) {
        return frameCount.value >= n;
    }
}