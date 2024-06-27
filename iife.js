const counter = (function () {
    let count = 0;
   
   
    return function () {
      count += 1;
   
   
      return count;
    };
   })();

counter(); // 1
counter(); // 2
counter(); // 3