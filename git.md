# git add fileName   
暂存区的目录树将被更新，将为改动的文件创建新的对象并存在对象库，index里面将存储对象所对应的索引
- git commit -m "commits"     	
暂存区的目录树写入对象库，master分支会做相应的更新，即master所指的目录树就是暂存区的目录树
```git
- git status -s
- git push -u origin master
- git reset HEAD
- git pull origin //获取更新
- git rm -r --cached target  从暂存区删除target文件夹
- git diff        查看尚未缓存的改动(未写入对象库的修改)
- git diff --cached    查看已经缓存的改动(写入对象库)
```
- 配置个人的用户名称和电子邮件地址：
```git
git config --global user.name "runoob"
git config --global user.email test@runoob.com
```
全局配置加 --global ,不加的话可为某目录设置其他git用户

- git --chechout <fileName>  用暂存区的该文件覆盖工作区的名为fileName的文件

- 查看版本
git tag 
- 切换到某个版本
git --checkout - tagName

- 代理设置   要注意ss ssr跑的是什么协议 http?https?sock5?
```git
git config --global http.proxy http://127.0.0.1:8123
git config --global https.proxy http://127.0.0.1:8123
git config --global --unset http.proxy
git config --global --unset https.proxy
git config delete proxy
```
- 查看仓库的config
You can use git config --list, or look at your ~/.gitconfig file. Local config will be in your repository's .git/config file.


- git tag
https://stackoverflow.com/questions/35979642/what-is-git-tag-how-to-create-tags-how-to-checkout-git-remote-tags


- 添加其他仓库的东西
`git remote add true-test https://github.com/ethereum/aleth`
- 获得true-test的更新
`git pull true-test`
- 合并
`git merge true-test/tagName`
- 查看合并冲突的文件
`git diff --name-status --diff-filter=U`

- 设置冲突处理工具
```git
git config merge.tool vimdiff
git config merge.conflictstyle diff3
git config mergetool.prompt false
```
- 处理冲突
git mergetool
Step 3: You will see a vimdiff display in following format

  +----------------------+
  |       |      |       |
  |LOCAL  |BASE  |REMOTE |
  |       |      |       |
  +----------------------+
  |      MERGED          |
  |                      |
  +----------------------+
These 4 views are

LOCAL – this is file from the current branch

BASE – common ancestor, how file looked before both changes

REMOTE – file you are merging into your branch

MERGED – merge result, this is what gets saved in the repo

选择哪个文件将被合并

If you want to get changes from REMOTE

:diffg RE  
If you want to get changes from BASE

:diffg BA  
If you want to get changes from LOCAL

:diffg LO 
Step 5. Save, Exit, Commit and Clean up
保存并退出
:wqa save and exit from vi


#主分支冲突
```git
git fetch origin
git pull origin master
git checkout --ours filename
git checkout --theirs filename
git add filename
git commit -m "use local/remote file"
```
- 取消合并分支
git reset --hard <commit_before_merge>  #修改head指向之前的commit


- 子模块更新
https://github.com/tj/git-extras/pull/80

- tag
删除远程的tag
git push --delete origin v0.0.0.1-gkchain

- 新建tag
git tag mytag master
- push新tag
git push origin <tag_name>

- 只克隆某个仓库的一个分支
git clone --single-branch --branch <branchname> host:/dir.git

- ignore不起作用
原因是.gitignore只对untack 的文件有效
git rm -r --cached .   #删除本地缓存

- 删除本地和远程分支
git branch -d debug1
git push origin --delete debug1

- 配置文件位置
~/.gitconfig
