function solution(id_pw, db) {
  const [id, pw] = id_pw;
  let idExists = false;
  let correctPw = false;
  for (let i = 0; i < db.length; i++) {
    const [dbId, dbPw] = db[i];

    if (dbId === id) {
      idExists = true;
      if (dbPw === pw) {
        correctPw = true;
        break;
      }
    }
  }

  if (correctPw) return 'login';
  if (idExists) return 'wrong pw';
  return 'fail';
}