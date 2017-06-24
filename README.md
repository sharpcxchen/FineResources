            LCBA version 0.1.5
    LCBA is a wrapper around dulwich. It provides an easy and familiar interface to git.
    It's pure python (no dependency on the ``git`` binary) and has no other dependencies besides
    the python stdlib, dulwich and paramiko (optional).
    1，对android资源的自动化优化，并解决若干lint及lint删除资源和内容引起的问题；
    2，并且我们还实现了对图片资源的压缩，极大的降低了内存使用空间，支持增量和自动化动化的压缩出处理，支持对apk进行资源混淆以再次节省空间；
    3，支持模块化的pip更新方式，模块化以便移植，未来还将自持ios的图片压缩；
    #怎样使用
    核心包我们已经更新到pip服务器，最新版本0.1.5
    >>1).安装依赖
    pip install lxml 
    pip install lcba
    pip install tinify
    brew install 7za （如果你不使用可以不用安装）
    #各个模块说明
