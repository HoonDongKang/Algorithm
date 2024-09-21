function solution([fy, fm, fd], [sy, sm, sd]) {
    return new Date(`${fy}-${fm}-${fd}`) >= new Date(`${sy}-${sm}-${sd}`) ? 0 : 1
}