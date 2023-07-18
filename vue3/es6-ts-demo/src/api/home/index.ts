import request from '@/utils/request';

/**
 * 查询随机笑话列表
 *
 * @param queryParams
 */
export function getMovieList() {
    return request({
        url: '/sjbz/api.php?lx=dongman&format=json',
        method: 'get'
    });
}

// /**
//  * 查询新闻列表
//  *
//  * @param queryParams
//  */
// export function getMovieList() {
//     return request({
//         url: '/api/joke/list?num=10',
//         method: 'get'
//     });
// }
//
// /**
//  * 查询随机水果列表
//  *
//  * @param queryParams
//  */
// export function getMovieList() {
//     return request({
//         url: '/api/joke/list?num=10',
//         method: 'get'
//     });
// }

