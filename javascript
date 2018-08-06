1.jquery源
  <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script>
2.promise
    promiseTest:function()
    {
        var p1=new Promise(function(resolve,reject)
            {
                var test=1;
                resolve(test);
            });
        p1.then(
            function(test){
            console.log(test);
            test++;
            return test;
        }).then(
        function(test){
            console.log(test);
            return [1,2,3];
        }).then(function(result)
        {
            console.log(result);
        });
    }
    注意：前一个then的返回值是后一个then的返回值，promise里面要调用resolve函数。
