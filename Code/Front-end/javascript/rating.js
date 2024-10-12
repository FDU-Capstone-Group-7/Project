// $(document).ready(function () {
//     let ratingValue = 0;

//     $('.star').on('click', function () {
//         ratingValue = $(this).data('value');
//         $('#rating-output').text(`Rating: ${ratingValue}`);
//         $('#submit-rating').prop('disabled', false); // 启用提交按钮
//     });

//     $('#submit-rating').on('click', function () {
//         // 提交评分到后端
//         $.ajax({
//             url: '/api/submit-rating',  // 替换为你的后端 API 路径
//             type: 'POST',
//             contentType: 'application/json',
//             data: JSON.stringify({ rating: ratingValue }),
//             success: function (response) {
//                 console.log('评分提交成功', response);
//                 // 禁用评分和提交按钮
//                 $('.star').off('click'); // 禁用星星点击
//                 $('#submit-rating').prop('disabled', true); // 禁用提交按钮
//             },
//             error: function (error) {
//                 console.error('Submission failed', error);
//             }
//         });
//     });
// });
