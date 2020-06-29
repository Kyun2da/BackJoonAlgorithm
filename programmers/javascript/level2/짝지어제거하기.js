const s = "baabaa";

const solution = (s) => {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack.length === 0 || stack[stack.length - 1] !== s[i]) {
      stack.push(s[i]);
    } else {
      stack.pop();
    }
  }

  if (stack.length === 0) {
    return 1;
  }
  return 0;
};

console.log(solution(s));
