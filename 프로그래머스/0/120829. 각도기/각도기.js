const acuteAngle = (angle) => (0 < angle) && (angle < 90);
const rightAngle = (angle) => angle === 90;
const obtuseAngle = (angle) => (90 < angle) && ( angle < 180);
const straightAngle = (angle) => angle === 180;

function solution(angle) {
    return acuteAngle(angle) ? 1 : rightAngle(angle) ? 2 : obtuseAngle(angle) ? 3 : straightAngle(angle) ? 4 : -1;
}