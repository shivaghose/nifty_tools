# dir_monch

Shortens paths to help keep your terminal neat and tidy.

```
shiva@scarlet: ~/git/nifty_tools  (master)
$ cd dir_monch/
shiva@scarlet: ~/g/n/dir_monch  (master)
$
```

_Dedicated to a monch of cold_

![https://s1.piq.land/2013/09/03/JMYxa1ULLmFHJrWvbcRslPNl_400x400.png](https://s1.piq.land/2013/09/03/JMYxa1ULLmFHJrWvbcRslPNl_400x400.png)

## Usage

Add this folder to your path. For example, you could add the following to your `.bashrc`:
```
export PATH="path/to/nifty_tools/dir_monch:$PATH"
```

Update your PS1 (might be in your `.bashrc` or your `.bash_profile`). For e.g. it could look like
```
export PS1="\u@\h: \$(dir_monch) \n\\$ \[$(tput sgr0)\]"
```

Voila! All done!
