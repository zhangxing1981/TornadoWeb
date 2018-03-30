 var boxList = [
   {
     id: '1',
     name: '电教馆'
   },
   {
     id: '2',
     name: '基础教育'
   },
   {
     id: '3',
     name: '专题教育'
   },
   {
     id: '4',
     name: '学籍系统'
   },
   {
     id: '5',
     name: '高中慕课'
   },
   {
     id: '6',
     name: '综评系统'
   },
   {
     id: '7',
     name: 'MOOR系统'
   },
   {
     id: '8',
     name: '电子书包'
   },
   {
     id: '11',
     name: '职业教育'
   },
   {
     id: '12',
     name: '终生教育'
   },
   {
     id: '13',
     name: '成人教育'
   },
   {
     id: '14',
     name: '学生'
   },
   {
     id: '15',
     name: '教师'
   },
   {
     id: '16',
     name: '管理者'
   },
   {
     id: '17',
     name: '决策者'
   }
 ]

 var relatList = [
    {
      id: '1',
      name: '服务领域'
    },
    {
      id: '2',
      name: '服务人群'
    },
    {
      id: '3',
      name: '相关项目'
    },
    {
      id: '4',
      name: '主办单位'
    },
    {
      id: '5',
      name: '关联机构'
    },
    {
      id: '6',
      name: '承建项目'
    },
    {
      id: '7',
      name: '使用系统'
    }
 ]

 var linkList = [
    {
      pid: 1,
      fid: 2,
      rid: 1
    },
    {
      pid: 1,
      fid: 11,
      rid: 1
    },
    {
      pid: 1,
      fid: 12,
      rid: 1
    },
    {
      pid: 1,
      fid: 13,
      rid: 1
    },
    {
      pid: 1,
      fid: 14,
      rid: 2
    },
    {
      pid: 1,
      fid: 15,
      rid: 2
    },
    {
      pid: 1,
      fid: 16,
      rid: 2
    },
    {
      pid: 1,
      fid: 17,
      rid: 1
    },
    {
      pid: 1,
      fid: 3,
      rid: 6
    },
    {
      pid: 1,
      fid: 4,
      rid: 6
    },
    {
      pid: 1,
      fid: 5,
      rid: 6
    },
    {
      pid: 1,
      fid: 6,
      rid: 6
    },
    {
      pid: 1,
      fid: 7,
      rid: 6
    },
    {
      pid: 1,
      fid: 8,
      rid: 6
    },
    {
      pid: 7,
      fid: 1,
      rid: 4
    },
    {
      pid: 7,
      fid: 15,
      rid: 2
    },
    {
      pid: 7,
      fid: 17,
      rid: 2
    },
    {
      pid: 7,
      fid: 17,
      rid: 2
    },
    {
      pid: 7,
      fid: 2,
      rid: 1
    },
    {
      pid: 13,
      fid: 1,
      rid: 5
    },
    {
      pid: 8,
      fid: 1,
      rid: 4
    },
    {
      pid: 8,
      fid: 14,
      rid: 2
    },
    {
      pid: 8,
      fid: 15,
      rid: 2
    },
    {
      pid: 8,
      fid: 2,
      rid: 1
    },
    {
      pid: 5,
      fid: 1,
      rid: 4
    },
    {
      pid: 5,
      fid: 14,
      rid: 2
    },
    {
      pid: 5,
      fid: 15,
      rid: 2
    },
    {
      pid: 5,
      fid: 17,
      rid: 2
    },
    {
      pid: 5,
      fid: 2,
      rid: 1
    },
    {
      pid: 15,
      fid: 1,
      rid: 5
    },
    {
      pid: 2,
      fid: 3,
      rid: 3
    },
    {
      pid: 2,
      fid: 4,
      rid: 3
    },
    {
      pid: 2,
      fid: 5,
      rid: 3
    },
    {
      pid: 2,
      fid: 6,
      rid: 3
    },
    {
      pid: 2,
      fid: 7,
      rid: 3
    },
    {
      pid: 2,
      fid: 8,
      rid: 3
    },
    {
      pid: 2,
      fid: 1,
      rid: 5
    },
    {
      pid: 15,
      fid: 3,
      rid: 3
    },
    {
      pid: 15,
      fid: 4,
      rid: 3
    },
    {
      pid: 15,
      fid: 5,
      rid: 3
    },
    {
      pid: 15,
      fid: 6,
      rid: 3
    },
    {
      pid: 15,
      fid: 7,
      rid: 3
    },
    {
      pid: 15,
      fid: 8,
      rid: 3
    },
    {
      pid: 15,
      fid: 1,
      rid: 5
    },
    {
      pid: 14,
      fid: 3,
      rid: 3
    },
    {
      pid: 14,
      fid: 4,
      rid: 3
    },
    {
      pid: 14,
      fid: 5,
      rid: 3
    },
    {
      pid: 14,
      fid: 6,
      rid: 3
    },
    {
      pid: 14,
      fid: 7,
      rid: 3
    },
    {
      pid: 14,
      fid: 8,
      rid: 3
    },
    {
      pid: 14,
      fid: 1,
      rid: 5
    },
    {
      pid: 17,
      fid: 1,
      rid: 5
    },
    {
      pid: 17,
      fid: 3,
      rid: 7
    },
    {
      pid: 17,
      fid: 4,
      rid: 7
    },
    {
      pid: 17,
      fid: 5,
      rid: 7
    },
    {
      pid: 17,
      fid: 6,
      rid: 7
    },
    {
      pid: 17,
      fid: 7,
      rid: 7
    },
    {
      pid: 4,
      fid: 1,
      rid: 4
    },
    {
      pid: 4,
      fid: 14,
      rid: 2
    },
    {
      pid: 4,
      fid: 15,
      rid: 2
    },
    {
      pid: 4,
      fid: 17,
      rid: 2
    },
    {
      pid: 4,
      fid: 2,
      rid: 1
    },
    {
      pid: 11,
      fid: 1,
      rid: 5
    },
    {
      pid: 12,
      fid: 1,
      rid: 5
    },
    {
      pid: 3,
      fid: 1,
      rid: 4
    },
    {
      pid: 3,
      fid: 14,
      rid: 2
    },
    {
      pid: 3,
      fid: 15,
      rid: 2
    },
    {
      pid: 3,
      fid: 17,
      rid: 2
    },
    {
      pid: 3,
      fid: 2,
      rid: 1
    },
    {
      pid: 6,
      fid: 1,
      rid: 4
    },
    {
      pid: 6,
      fid: 14,
      rid: 2
    },
    {
      pid: 6,
      fid: 15,
      rid: 2
    },
    {
      pid: 6,
      fid: 17,
      rid: 2
    },
    {
      pid: 6,
      fid: 2,
      rid: 1
    },
    {
      pid: 16,
      fid: 1,
      rid: 5
    }
 ]