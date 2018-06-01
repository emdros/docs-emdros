#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([emdros-docs], [4.0.0], [ulrikp@scripturesys.com])
AC_CONFIG_MACRO_DIRS([m4])
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([doc/lyx/MQL-Programmers-Guide.lyx])

AC_CHECK_PROGS(LYX, [lyx], no)
if test x$LYX = xno; then
  AC_MSG_ERROR([ERROR: lyx must be installed for this package to be built.])
fi
AC_SUBST(LYX)


AC_CHECK_PROGS(PYTHON, [python2.7 python27 python2.6 python26 python2.5 python25 python2.4 python24 python2.3 python23 python], no)
if test x$PYTHON = xno; then
  AC_MSG_ERROR([ERROR: Python 2.x must be installed for this package to be built.])
fi
AC_SUBST(PYTHON)



AC_CHECK_PROGS(ZIP, [zip], no)
if test x$ZIP = xno; then
  AC_MSG_ERROR([ERROR: zip must be installed for this package to be built.])
fi
AC_SUBST(ZIP)



AC_CHECK_PROGS(PDFLATEX, [pdflatex], no)
if test x$PDFLATEX = xno; then
  AC_MSG_ERROR([ERROR: pdflatex must be installed for this package to be built.])
fi
AC_SUBST(PDFLATEX)


AC_CONFIG_FILES([Makefile
		 doc/Makefile
		 doc/progref/Makefile
		 doc/importtool/Makefile
		 doc/querytool/Makefile
               ])
AC_OUTPUT
