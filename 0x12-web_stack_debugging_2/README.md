
# 0x12. Web stack debugging #2
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_p2T2zTZ84qKVA9F_J95hpmf2GTKTPuiAvx0KkUCEzJ_IxLBNl9din2Q8Bgn4bwT4Jlg&usqp=CAU)
## 0. Run software as another user
The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

