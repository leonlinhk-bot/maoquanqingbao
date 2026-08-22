; (function (app) {
    $.ajax({
        type: 'get',
        url: '../../view/components/sts.html?' + (+ new Date),
        success: function (res) {

        },
        error: function (res) {

        }
    });
    
    function isGuiZhang(arr) {
        if (!arr || !(arr instanceof Array)) {
            return false;
        }
        for (var  i = 0; i < arr.length; i++) {
            if(arr[i].ItemID == 4214){
                return true;
            }
        }
        return false;
    }
 
    app.controller('itemListCtrl', function ($scope, global,$timeout) {
        var itemId = getParam("itemId");
        var itemUrl = getParam("itemUrl");
        var itemPId = getParam("itemPId");
        var itemName = getParam("itemName");
    

        var itemsubPId = getParam("itemsubPId");
        

        $scope.itemId = itemId;
        $scope.itemUrl = itemUrl;
        $scope.itemPId = itemPId;
        $scope.itemName = itemName;
        $scope.itemsubPId = itemsubPId;
        
    
        global.getCDN({ url: '/item/getItemNameById', params: {itemId: itemId } }, function (res) { 
            if (res.rptCode === 200 && res.data) {
                if(res.data.itemUrl && $scope.itemUrl != res.data.itemUrl){
                    global.getCDN({ url: '/Skin/getSysParams' }, function (res1) {
                        if(res1.rptCode == 200 && res1.data && res1.data.cn_column_router){ 
                            if(!findSingleRouter(res1.data.cn_column_router, $scope.itemUrl)) {
                                window.location.href = '/404.html'
                            }
                        }
                    })
                }
            }
        })
       

        global.getCDN({ url: '/item/getLeftMenuItem', params: { itemID: itemPId } }, function (res) {
            if (res.rptCode == 200) {
                for (var i = 0; i < res.data.length; i++) {
                    res.data[i].parsedUrl = global.parseItemUrl2(res.data[i]);
                    for (var j = 0; j < res.data[i].subItemslist.length; j++) {
                        res.data[i].subItemslist[j].parsedUrl = global.parseItemUrl2(res.data[i].subItemslist[j], res.data[i].itemPid);
                    }

                    //栏目名称、描述、关键字、种类
                    if (res.data[i].itemName == itemName) {
                        $("head > meta[name='ColumnName']").attr("content", res.data[i].itemName);
                        $("head > meta[name='ColumnDescription']").attr("content", res.data[i].desc);
                        $("head > meta[name='ColumnKeywords']").attr("content", res.data[i].keyword);
                        $("head > meta[name='ColumnType']").attr("content", res.data[i].type);
                    }
                }
                $scope.menuData = res.data;
                $scope.itemPName = global.getItemNameById2(itemPId, 1);
            }
        });

        //列表页面包屑
        global.getCDN({ url: '/item/getItemBread', params: { itemId: itemId } }, function (data) {
            if (data && data.rptCode == 200 && data.data && data.data.length) {
                data.data[data.data.length - 1].itemUrl = "";
                $scope.breadcrumb_detail = data.data;
            } else {
                window.location.href = '/404.html'
            }
        }, function () {
            window.location.href = '/404.html'
        });
    });

    app.controller('itemListRightListCtrl', function ($scope, global, $timeout) {
        //list列表页模板-监管动态、公告通知、行政许可、行政处罚、办事指南、统计信息
        var itemId = getParam("itemId");
        var itemUrl = getParam("itemUrl");
        var itemPId = getParam("itemPId");
        var itemsubPId = getParam("itemsubPId");
        var generaltype = getParam("generaltype");
        var itemsubPName = getParam("itemsubPName");   //行政许可、行政处罚专用

        $scope.itemId = itemId;
        $scope.itemUrl = itemUrl;
        $scope.itemPId = itemPId;
        $scope.itemsubPId = itemsubPId;
        $scope.generaltype = generaltype;
        $scope.itemsubPName = itemsubPName;


        global.getCDN({ url: '/item/getItemNameById', params: {itemId: itemId } }, function (res) { 
            $scope.itemNewName = '';
            if (res.rptCode === 200 && res.data) {
                $scope.itemNewName = res.data.itemName;
            }
        })
        if(itemsubPName){
            global.getCDN({ url: '/item/getItemNameById', params: {itemId: itemsubPId } }, function (res) {
                $scope.itemsubPNewName = '';
                if (res.rptCode === 200 && res.data) {
                        $scope.itemsubPNewName = res.data.itemName;
                    
                }
            })
           
        }else{
            $scope.itemsubPNewName= ''
        }
        
        var itemName = ""

        if (itemName == undefined || itemName === '') {
            global.getCDN({
                url: '/item/getLeftMenuItem',
                params: { itemID: itemPId }
            }, function (res) {
                for (var i = 0; i < res.data.length; i++) {
                    if (res.data[i].itemId == itemId) {
                        $scope.itemName = res.data[i].itemName;
                        $scope.itemId = res.data[i].itemId;
                        break;
                    }
                    for (var j = 0; j < res.data[i].subItemslist.length; j++) {
                        if (res.data[i].subItemslist[j].itemId == itemId) {
                            $scope.itemName = res.data[i].subItemslist[j].itemName;
                            $scope.itemId = res.data[i].subItemslist[j].itemId;
                            break;
                        }
                    }
                }
            })
        } else {
            $scope.itemName = itemName;
            $scope.itemId = itemId;
        }

        var pageIndex2 = global.getPageIndex2();
        $scope.pager = {
            itemNum: 0, // 数据总条数
            pageItemNum: 18, // 每页条数
            currentPageIndex: pageIndex2, // 当前页码
            displayPageNum: 3, // pager显示页数
            jumpInputenterval: '',
            pageIndexChange: function (pageIndex2, dataReceived) {
                global.getCDN({ url: '/DocInfo/SelectDocByItemIdAndChild', params: { itemId: itemId, pageSize: 18, pageIndex: pageIndex2 } }, function (data) {
                    if (data.rptCode == 200) {
                        $scope.data = data.data.rows;
                        dataReceived(data.data.total);
                    } else {
                        console.log(data);
                    }
                }, function (data) {
                    console.log(data);
                });
            }
        }
        $scope.fileTypeDownload = function (docId,type) {
          var zcfg = itemId == 927 ? 0 : 1;
          var file_urlnew = '';
          global.getCDN({ url: '/DocInfo/SelectByDocId', params: { docId: docId } }, function (data) {
            if (data.rptCode == 200) {
              // type是true为word  是false 为pdf
              if(isGuiZhang(data.data.listTwoItem)) { //规章
                file_urlnew = type ? '/cbircweb/download/downloadguizDoc': '/cbircweb/download/downloadguizPdf'
              }else {
                file_urlnew = type ? '/cbircweb/download/downloadDoc': '/cbircweb/download/downloadPdf'
              }
              $.ajax({
                url: file_urlnew,
                type:"GET",
                data:{docId:docId,zcfg:zcfg,itemId:itemId},
                error: function (xhr, error, ex) {
                    if (xhr.status == '200') {
                        window.location.href = file_urlnew;
                    } else if (xhr.status == '404') {
                        alert("文件不存在！")
                    }
                },
                success: function () {
                    window.location.href = file_urlnew+ "?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
                }
            });
            }
          }, function (data) {
              console.log(data);
          });
        }
        $scope.pdfFileDownload = function (docId,isGz) {
            if(itemId==927){
                var zcfg=0;
            }else{
                var zcfg=1;
            }
    
            var file_urlnew= isGz == '1' ? '/cbircweb/download/downloadguizPdf' : "/cbircweb/download/downloadPdf" ;

            $.ajax({
                url: file_urlnew,
                type:"GET",
                data:{docId:docId,zcfg:zcfg,itemId:itemId},
                error: function (xhr, error, ex) {
                    if (xhr.status == '200') {
                        window.location.href = file_urlnew;
                    } else if (xhr.status == '404') {
                        alert("文件不存在！")
                    }
                },
                success: function () {
                    window.location.href = file_urlnew+"?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
                }
            });
        }
        //  文章word下载new
        $scope.docFileDownload = function (docId,isGz) {
            if(itemId==927){
                var zcfg=0;
            }else{
                var zcfg=1;
            }
          
            var file_urlnew= isGz == '1' ? '/cbircweb/download/downloadguizDoc' : "/cbircweb/download/downloadDoc";
            $.ajax({
                url: file_urlnew,
                type:"GET",
                data:{docId:docId,zcfg:zcfg,itemId:itemId},
                error: function (xhr, error, ex) {
                    if (xhr.status == '200') {
                        window.location.href = file_urlnew;
                    } else if (xhr.status == '404') {
                        alert("文件不存在！")
                    }else if (xhr.status == '423') {
                        alert("文件尚未生成！")
                    }
                },
                success: function () {
                    window.location.href = file_urlnew+"?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
                }
            });
        }

        //判断url是否是404
        $scope.fileDownload = function (file_url) {
            $.ajax({
                url: file_url,
                error: function (xhr, error, ex) {
                    if (xhr.status == '200') {
                        window.location.href = file_url;
                    } else if (xhr.status == '404') {
                        alert("文件不存在！")
                    }
                },
                success: function () {
                    window.location.href = file_url;
                }
            });
        }

    });

    app.controller('itemListRightArticleCtrl', function ($scope, global, $timeout) {
        //内容列表页模板-法律声明、主要职责
        var itemId = getParam("itemId");
        var itemUrl = getParam("itemUrl");
        var itemPId = getParam("itemPId");
        var itemsubPId = getParam("itemsubPId");
        var itemName = getParam("itemName")
      
        $scope.itemId = itemId;
        $scope.itemUrl = itemUrl;
        $scope.itemPId = itemPId;
        $scope.itemsubPId = itemsubPId;

        global.getCDN({ url: '/item/getLeftMenuItem', params: { itemID: itemPId } }, function (res) {
            if (res.rptCode == 200) {
                for (var i = 0; i < res.data.length; i++) {
                    res.data[i].parsedUrl = global.parseItemUrl2(res.data[i]);
                    for (var j = 0; j < res.data[i].subItemslist.length; j++) {
                        res.data[i].subItemslist[j].parsedUrl = global.parseItemUrl2(res.data[i].subItemslist[j], res.data[i].itemPid);
                    }
                }
                $scope.menuData = res.data;
            }
        });

        global.getCDN({ url: '/DocInfo/SelectDocEntityByItemId', params: { "itemId": itemId } }, function (res) {
            if (res.rptCode == 200 && res.data != null) {
                global.getCDN({ url: '/DocInfo/SelectByDocId', params: { docId: res.data.docId } }, function (res) {
                    if (res.rptCode == 200) {
                        $scope.data = res.data;
                        if (res.data.docUuid == "" || res.data.docUuid == null) {
                            $scope.showTitle = true;
                        } else {
                            $scope.showTitle = false;
                        }
                        //wenzhang-content是否加上white-space
                        if (res.data.publishDate < '2019-09-01' || res.data.docUuid != null) {
                            $scope.isWhite_space = false;
                        } else {
                            $scope.isWhite_space = true;
                        }
                           //  文章类型展示
                switch (res.data.documentType) {
                    case "0":
                      $scope.documentTypeDetail="原创";
                        break;
                    case "1":
                      $scope.documentTypeDetail="转载";
                        break;  
                    case "2":
                       $scope.documentTypeDetail="编译";
                        break;
                    default:
                        $scope.documentTypeDetail="摘录";
                        break;
                }
                    }
                }, function (res) {
                    console.log(res);
                });
            } else {
                console.log(res);
            }
        }, function (res) {
            console.log(res);
        });
    });

    app.controller('itemListRightMoreCtrl', function ($scope, global, $timeout) {
        //more列表页模板-政策法规
        var itemId = getParam("itemId");
        var itemUrl = getParam("itemUrl");
        var itemPId = getParam("itemPId");
        var itemsubPId = getParam("itemsubPId");
        var itemName = getParam("itemName");
       
        $scope.itemId = itemId;
        $scope.itemUrl = itemUrl;
        $scope.itemPId = itemPId;
        $scope.itemsubPId = itemsubPId;

        
        global.getCDN({ url: '/item/getItemNameById', params: {itemId: itemId } }, function (res) {
            $scope.itemNewName = '';
            if (res.rptCode === 200 && res.data) {
                $scope.itemNewName = res.data.itemName;
            }
        })


        if (itemName == undefined || itemName === '') {
            global.getCDN({
                url: '/item/getLeftMenuItem',
                params: { itemID: itemPId }
            }, function (res) {
                for (var i = 0; i < res.data.length; i++) {
                    if (res.data[i].itemId == itemId) {
                        $scope.itemName = res.data[i].itemName;
                        break;
                    }
                    for (var j = 0; j < res.data[i].subItemslist.length; j++) {
                        if (res.data[i].subItemslist[j].itemId == itemId) {
                            $scope.itemName = res.data[i].subItemslist[j].itemName;
                            break;
                        }
                    }
                }
            })
        } else {
            $scope.itemName = itemName;
        }

        global.getCDN({ url: '/DocInfo/SelectItemAndDocByItemPId', params: { "pageSize": 3, "itemId": itemId } }, function (data) {
            if (data.rptCode == 200) {
                $scope.data = data.data;
            } else {
                console.log(data);
            }
        }, function (data) {
            console.log(data);
        });
           //  文章pdf下载new
    $scope.fileTypeDownload = function (docId,itemId,type) {
      var zcfg = itemId == 927 ? 0 : 1;
      var file_urlnew = '';
      global.getCDN({ url: '/DocInfo/SelectByDocId', params: { docId: docId } }, function (data) {
        if (data.rptCode == 200) {
          // type是true为word  是false 为pdf
          if(isGuiZhang(data.data.listTwoItem)) { //规章
            file_urlnew = type ? '/cbircweb/download/downloadguizDoc': '/cbircweb/download/downloadguizPdf'
          }else {
            file_urlnew = type ? '/cbircweb/download/downloadDoc': '/cbircweb/download/downloadPdf'
          }
          $.ajax({
            url: file_urlnew,
            type:"GET",
            data:{docId:docId,zcfg:zcfg,itemId:itemId},
            error: function (xhr, error, ex) {
                if (xhr.status == '200') {
                    window.location.href = file_urlnew;
                } else if (xhr.status == '404') {
                    alert("文件不存在！")
                }
            },
            success: function () {
                window.location.href = file_urlnew+ "?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
            }
        });
        }
      }, function (data) {
          console.log(data);
      });
    }
         
    $scope.pdfFileDownload = function (docId,itemId,isGz) {
        if(itemId==927){
            var zcfg=0;
        }else{
            var zcfg=1;
        }

        var file_urlnew= isGz == '1' ? '/cbircweb/download/downloadguizPdf' : "/cbircweb/download/downloadPdf" ;
        $.ajax({
            url: file_urlnew,
            type:"GET",
            data:{docId:docId,zcfg:zcfg,itemId:itemId},
            error: function (xhr, error, ex) {
                if (xhr.status == '200') {
                    window.location.href = file_urlnew;
                } else if (xhr.status == '404') {
                    alert("文件不存在！")
                }
            },
            success: function () {
                window.location.href = file_urlnew+ "?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
            }
        });
    }
    //  文章word下载new
    $scope.docFileDownload = function (docId,itemId,isGz) {
        if(itemId==927){
            var zcfg=0;
        }else{
            var zcfg=1;
        }
        var file_urlnew= isGz == '1' ? '/cbircweb/download/downloadguizDoc' : "/cbircweb/download/downloadDoc" ;
     
        $.ajax({
            url: file_urlnew,
            type:"GET",
            data:{docId:docId,zcfg:zcfg,itemId:itemId},
            error: function (xhr, error, ex) {
                if (xhr.status == '200') {
                    window.location.href = file_urlnew;
                } else if (xhr.status == '404') {
                    alert("文件不存在！")
                }else if (xhr.status == '423') {
                    alert("文件尚未生成！")
                }
            },
            success: function () {
                window.location.href = file_urlnew+ "?docId=" + docId+"&zcfg="+zcfg+"&itemId="+itemId;
            }
        });
    }
        //判断下载是否是404
        $scope.fileDownload = function (file_url) {
            $.ajax({
                url: file_url,
                error: function (xhr, error, ex) {
                    if (xhr.status == '200') {
                        window.location.href = file_url;
                    } else if (xhr.status == '404') {
                        alert("文件不存在！")
                    }
                },
                success: function () {
                    window.location.href = file_url;
                }
            });
        }
        
    });
})(app);