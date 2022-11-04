


$(function(){
    
    $('.addToCartbtn').on("click",function (e){
        e.preventDefault();
        console.log("it is working")
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty-input').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method:"POST",
            url:"/add-to-cart",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken:token,
            },
            
            success:function(response){
                console.log(response)
            }


        })
    });
});

