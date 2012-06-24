
%define py_ver         2.2
%define py_prefix      %{_prefix}
%define py_libdir      %{py_prefix}/lib/python%{py_ver}
%define py_incdir      %{_includedir}/python%{py_ver}
%define py_sitedir     %{py_libdir}/site-packages
%define py_dyndir      %{py_libdir}/lib-dynload
%define py_comp        ./python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"
%define py_ocomp       ./python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"
 
Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfl�che
Summary(fr):	Langage de script de t�s haut niveau avec interface X
Summary(pl):	Python - j�zyk obiektowy wysokiego poziomu
Summary(tr):	X aray�zl�, y�ksek d�zeyli, kabuk yorumlay�c� dili
Name:		python
Version:	%{py_ver}b2
Release:	1
License:	PSF
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
URL:		http://www.python.org/
Source0:	http://prdownloads.sourceforge.net/python/Python-%{version}.tgz
Source1:	http://www.python.org/ftp/python/doc/%{version}/html-%{version}.tar.bz2
Source2:	%{name}-setup.dist
Patch0:		%{name}-shared-lib.patch
Patch1:		%{name}-dl_global.patch
Patch2:		%{name}-setup-install.patch
Patch3:		%{name}-readline.patch
Patch4:		%{name}-pythonpath.patch
Patch5:		%{name}-notermcap.patch
Patch6:		%{name}-ac25x.patch
Patch7:		%{name}-default_encoding.patch
BuildRequires:	XFree86-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.0.8-7
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.6b
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tix-devel
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	zlib-devel
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	db3-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	python-xml
Obsoletes:	python-intl
Obsoletes:	python-curses
Obsoletes:	python-gdbm
Obsoletes:	python-zlib
Obsoletes:	python2
Obsoletes:	python2-devel

%description
Python is an interpreted, interactive, object-oriented programming
language. It incorporates modules, exceptions, dynamic typing, very
high level dynamic data types, and classes. Python combines remarkable
power with very clear syntax. It has interfaces to many system calls
and libraries, as well as to various window systems, and is extensible
in C or C++. It is also usable as an extension language for
applications that need a programmable interface. Finally, Python is
portable: it runs on many brands of UNIX, on the Mac, and on PCs under
MS-DOS, Windows, Windows NT, and OS/2.

%description -l de
Python ist eine interpretierte, interaktive, objektorientierte
Programmiersprache, vergleichbar zu Tcl, Perl, Scheme oder Java.
Python enth�lt Module, Klassen, Exceptions, High-Level dynamische
Datentypen und dynamisches Typisieren. Python unterst�tzt Interfaces
zu vielen Systemaufrufen und Libraries, sowie verschiedene
Fenstersysteme (X11, Motif, Tk, Mac und MFC)

Programmierer k�nnen neue built-in-Module f�r Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache f�r Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses
Paket enth�lt die meisten Standard-Python-Module, und Module zum
Ansprechen von Tix (Tk-widget set) und RPM.

Dokumentationen zu Python sind in python-doc enthalten.

%description -l fr
Python est un langage de script interpr�t� et orient� objet. Il g�re
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles biblioth�ques syst�mes
avec du code C est simple, ce qui rend Python facile � utiliser dans
des configs personnalis�es.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfa�age avec les widgets Tix pour Tk
et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
j�zykiem programowania. Jest modularny, obs�uguje wyj�tki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python ��czy w
sobie du�e mo�liwo�ci i przejrzyst� sk�adni�. Posiada interfejsy do
wielu wywo�a� systemowych i bibliotek, w tym r�wnie� do r�nych
bibliotek okienkowych. Mo�liwo�ci jego mo�na jeszcze rozszerza�
poprzez odpowiednie modu�y pisane w C lub C++. Python mo�e by� r�wnie�
u�yty jako element aplikacji, kt�rym potrzebny jest interpreter do
skrypt�w. I wreszcie, Python jest wieloplatformowy, dzia�a na wielu
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

%description -l tr
Python, nesneye y�nelik bir kabuk yorumlay�c�d�r. Nesnelerin,
s�n�flar�n, mod�llerin ve ayk�r� durumlar�n dinamik y�klenmelerine
destek verir. C koduyla birlikte kullan�m� son derece kolayd�r. Bu
paket, standart Python birimlerinin �o�unun yan�s�ra Tk ve RPM i�in
aray�z birimlerini de i�erir.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr):	Biblioth�ques et en-t�tes pour construire du code python
Summary(pl):	Pliki nag��wkowe i biblioteki Pythona
Summary(tr):	Python ile geli�tirme yapmak i�in gerekli dosyalar
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This packages
contains the header files and libraries which are needed to do both of
these tasks.

%description -l de devel
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und l��t sich in andere Programme
integrieren. Dieses Paket enth�lt die Header-Dateien und Libraries,
die f�r beide Aufgaben erforderlich sind.

%description -l fr devel
L'interpr�teur Python est relativement facile � �tendre avec des
extensions charg�es dynamiquement et � ins�rer dans d'autres
programmes. Ce paquetage contient les en-t�tes et les biblioth�ques
n�cessaires � ces deux t�ches.

%description -l pl devel
Wszystko co potrzebne, aby napisa� w C/C++ modu� rozszerzaj�cy
mo�liwo�ci Pythona. S� tu r�wnie� wersje �r�d�owe modu��w ze
standardowej biblioteki.

%description -l tr devel
Bu paket, Python ile geli�tirme yap�labilmesi i�in gerekli ba�l�k
dosyalar�n� ve kitapl�klar� i�erir.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name}-devel = %{version}

%description static
Static python library.

%description static -l pl
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python 
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Pythona 
Summary(tr):	Python belgeleri
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Requires:	%{name} = %{version}
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description -l de doc
Dieses Paket enth�lt Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description -l fr doc
Ce paquetage contient la documentation sur le langage python et sur
son interpr�teur sous forme de fichiers ASCII et LaTeX.

%description -l pl doc
Oficjalna dokumentacja do Pythona. Zawiera przyk�adowe programy,
narz�dzia i dokumentacj�. Strony podr�cznika man znajduj� si� w
g��wnym pakiecie. Ten pakiet nie zawiera �r�de� dokumentacji
napisanych w LaTeX'u, tylko gotowe do wykorzystania pliki
postscript'owe i HTML.

%description -l tr doc
Bu paket, Python dili ile ilgili belgeleri ve d�z ASCII dosyalar� ve
LaTeX kaynaklar�n�n bir kar���m� olan yorumlay�c�y� i�erir.

#%package without-thread
#Summary:	Python without threads
#Summary(pl):	Pyton bez w�tk�w
#Group:          Development/Languages
#Group(de):      Entwicklung/Sprachen
#Group(pl):      Programowanie/J�zyki
#Requires:       %{name} = %{version}
#Obsoletes:      python-without-thread

#%description without-thread
#This package is rather needed for apache-mod_python module.
#Other ways of use are unknown.

#%description -l pl without-thread
#Pyton bez w�tk�w jest w�a�ciwie potrzebny
#tylko modu�owi apache-mod_python, bo apache nie
#ich na razie nie wspiera.

%package -n tkinter
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfl�che f�r Python
Summary(fr):	Interface graphique pour python.
Summary(pl):	Modu�y niskiego poziomu dla pakietu Python-tkinter
Summary(tr):	Python i�in grafik kullan�c� aray�z�
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}
Requires:	tcl >= 8.0.3 
Requires:	tk  >= 8.0.3
Requires:	tix >= 4.1.0.6

%description -n tkinter
This is the lowlevel C module that interfaces Tk and which is the
basis for the Tkinter, Python's OO interface to Tk, which is included
in the package python-tkinter.

The only reason this file is removed from python-tkinter, is to make
it more easy to replay _tkinter with a PIL (Python Imaging Libary)
aware version of it. Look at my PIL distribution.

%description -l de -n tkinter
Eine grafische Schnittstelle f�r Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description -l fr -n tkinter
Interface graphique pour Python, bas�e sur Tcl/Tk et utilis�e par
beaucoup des outils de configuration.

%description -l pl -n tkinter 
Ten pakiet zawiera modu�y w C, kt�re po�rednicz� w wywo�aniach
pomi�dzy samym Tk a modu�em Tkinter b�d�cym g��wnym interfejsem Tk dla
Pythona.

Jedynym powodem wydzielenia tego pakietu jest u�atwienie wymiany go na
PIL (Python Imaging Library).

%description -l tr -n tkinter
Python i�in Tcl/Tk'ye dayal� ve pek �ok ayarlama arac� taraf�ndan
kullan�lan grafik bir aray�zd�r.

%package old
Summary:	Depreciated Python modules
Summary(pl):	Nieaktualne modu�y j�zyka Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}

%description old
Install this package when one of your program written in Python is old
as Miss Universum of 1918, who only you want to see... ooops, which
only you want to run.

%description -l pl old
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich program�w napisanych
w j�zyku Python jest tak stary jak Miss Universum z roku 1918, kt�r�
tylko ty chcesz zobaczy�... przepraszam, kt�ry tylko ty chcesz
uruchomi�.

%package examples
Summary:	Example programs in Python
Summary(pl):	Przyk�adowe programy w Pythonie
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name}-devel = %{version}
Obsoletes:	python-tools

%description examples
Example programs in Python

%description -l pl examples
Przyk�adowe programy w Pythonie

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

install -d html-doc
tar -xf %{SOURCE1} --use=bzip2 -C html-doc

install %{SOURCE2} Modules/Setup

%build
export POSIXLY_CORRECT=TRUE

echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

autoconf

CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/db3"; export CPPFLAGS
%configure \
	--with-threads 

%{__make} OPT="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

export LD_LIBRARY_PATH=$(pwd)
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SCRIPTDIR=$RPM_BUILD_ROOT%{_libdir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	CONFINCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}

install libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}

%py_comp $RPM_BUILD_ROOT%{py_libdir}
%py_ocomp $RPM_BUILD_ROOT%{py_libdir}

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a

install -d $RPM_BUILD_ROOT%{_examplesdir}/python
cp -ar Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/python

gzip -9nf Misc/{ACKS,BLURB,BLURB.LUTZ,NEWS,HYPE,README,unicode.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpython*so.*
%{_mandir}/man1/*

%dir %{py_sitedir}
%dir %{py_libdir}
%{py_libdir}/*.py?
 
%dir %{py_dyndir}
%attr(755,root,root) %{py_dyndir}/[a-z]*.so
%attr(755,root,root) %{py_dyndir}/_te*.so
%attr(755,root,root) %{py_dyndir}/_[a-su-z]*.so

%dir %{py_libdir}/plat-*
%attr(755,root,root) %{py_libdir}/plat-*/regen
%{py_libdir}/plat-*/*.py?

%dir %{py_libdir}/curses
%{py_libdir}/curses/*.py?

%dir %{py_libdir}/distutils
%{py_libdir}/distutils/*.py?

%dir %{py_libdir}/distutils/command
%{py_libdir}/distutils/command/*.py?

%dir %{py_libdir}/encodings
%{py_libdir}/encodings/*.py?

%dir %{py_libdir}/xml
%{py_libdir}/xml/*.py?

%dir %{py_libdir}/xml/parsers
%{py_libdir}/xml/parsers/*.py?

%dir %{py_libdir}/xml/sax
%{py_libdir}/xml/sax/*.py?

%dir %{py_libdir}/xml/dom
%{py_libdir}/xml/dom/*.py?

%files devel
%defattr(644,root,root,755)
%doc Misc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{py_incdir}
%{py_incdir}/*.h
%attr(-,root,root) %{py_libdir}/*.py
%{py_libdir}/plat-*/*.py
%{py_libdir}/curses/*.py
%{py_libdir}/distutils/*.py
%{py_libdir}/distutils/command/*.py
%{py_libdir}/xml/*.py
%{py_libdir}/xml/parsers/*.py
%{py_libdir}/xml/sax/*.py
%{py_libdir}/xml/dom/*.py
%{py_libdir}/encodings/*.py

%dir %{py_libdir}/config
%attr(755,root,root) %{py_libdir}/config/makesetup
%attr(755,root,root) %{py_libdir}/config/install-sh
%{py_libdir}/config/Makefile
%{py_libdir}/config/Makefile.pre.in
%{py_libdir}/config/Setup
%{py_libdir}/config/Setup.config
%{py_libdir}/config/Setup.local
%{py_libdir}/config/config.c
%{py_libdir}/config/config.c.in
%{py_libdir}/config/python.o

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/Tools
%{_examplesdir}/python/Demo

%files doc
%defattr(644,root,root,755)
%doc html-doc/*
%dir %{py_libdir}/test
%attr(-,root,root) %{py_libdir}/test/*

%files -n tkinter
%defattr(644,root,root,755)

%{py_libdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so

%files old
%defattr(644,root,root,755)

%dir %{py_libdir}/lib-old
%{py_libdir}/lib-old/*.py?
