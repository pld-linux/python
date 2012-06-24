Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfl�che
Summary(fr):	Langage de script de t�s haut niveau avec interface X.
Summary(pl):	Python - j�zyk obiektowy wysokiego poziomu
Summary(tr):	X aray�zl�, y�ksek d�zeyli, kabuk yorumlay�c� dili
Name:		python
Version:	1.5.2
Release:	17
Copyright:	Distributable
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
URL:		http://www.python.org/
Source0:	ftp://ftp.python.org/pub/python/src/py152.tgz
Source1:	Python-Doc.tar.gz
Source2:	cursesmodule.c
Patch0:		python-pld.patch
Patch1:		python-sed.patch
Patch2:		python-dl_global.patch
Patch3:		python-wdb.patch
Patch4:		python-wuftpd.patch
BuildRequires:	XFree86-devel
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	tix
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python is an interpreted, interactive, object-oriented programming
language. It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface. Finally, Python is portable: it runs on many
brands of UNIX, on the Mac, and on PCs under MS-DOS, Windows, Windows NT,
and OS/2.

%description -l de
Python ist eine interpretierte, interaktive, objektorientierte
Programmiersprache, vergleichbar zu Tcl, Perl, Scheme oder Java. Python
enth�lt Module, Klassen, Exceptions, High-Level dynamische Datentypen und
dynamisches Typisieren. Python unterst�tzt Interfaces zu vielen
Systemaufrufen und Libraries, sowie verschiedene Fenstersysteme (X11,
Motif, Tk, Mac und MFC)

Programmierer k�nnen neue built-in-Module f�r Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache f�r Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses Paket
enth�lt die meisten Standard-Python-Module, und Module zum Ansprechen von
Tix (Tk-widget set) und RPM.

Dokumentationen zu Python sind in python-doc enthalten.

%description -l fr
Python est un langage de script interpr�t� et orient� objet. Il g�re le
chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles biblioth�ques syst�mes avec
du code C est simple, ce qui rend Python facile � utiliser dans des configs
personnalis�es.

Ce paquetage Python contient la plupart des modules Python standards, ainsi
que ceux permettant l'interfa�age avec les widgets Tix pour Tk et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
j�zykiem programowania. Jest modularny, obs�uguje wyj�tki, dynamiczne typy,
zaawansowane dynamiczne struktury danych i klasy. Python ��czy w sobie du�e
mo�liwo�ci i przejrzyst� sk�adni�. Posiada interfejsy do wielu wywo�a�
systemowych i bibliotek, w tym r�wnie� do r�nych bibliotek okienkowych.
Mo�liwo�ci jego mo�na jeszcze rozszerza� poprzez odpowiednie modu�y pisane
w C lub C++. Python mo�e by� r�wnie� u�yty jako element aplikacji, kt�rym
potrzebny jest interpreter do skrypt�w. I wreszcie, Python jest
wieloplatformowy, dzia�a na wielu odmianach UNIX'a, Mac'u oraz PC pod
DOS'em, Windows, WindowsNT oraz OS/2.

%description -l tr
Python, nesneye y�nelik bir kabuk yorumlay�c�d�r. Nesnelerin, s�n�flar�n,
mod�llerin ve ayk�r� durumlar�n dinamik y�klenmelerine destek verir. C
koduyla birlikte kullan�m� son derece kolayd�r. Bu paket, standart Python
birimlerinin �o�unun yan�s�ra Tk ve RPM i�in aray�z birimlerini de i�erir.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr):	Biblioth�ques et en-t�tes pour construire du code python
Summary(pl):	Pliki nag��wkowe i biblioteki Python'a
Summary(tr):	Python ile geli�tirme yapmak i�in gerekli dosyalar
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically loaded
extensions and to embed in other programs. This packages contains the
header files and libraries which are needed to do both of these tasks.

%description -l de devel
Der Python-Interpretierer ist relativ einfach anhand von dynamisch ladbaren
Erweiterungen auszubauen und l��t sich in andere Programme integrieren.
Dieses Paket enth�lt die Header-Dateien und Libraries, die f�r beide
Aufgaben erforderlich sind.

%description -l fr devel
L'interpr�teur Python est relativement facile � �tendre avec des extensions
charg�es dynamiquement et � ins�rer dans d'autres programmes. Ce paquetage
contient les en-t�tes et les biblioth�ques n�cessaires � ces deux t�ches.

%description -l pl devel
Wszystko co potrzebne, aby napisa� w C/C++ modu� rozszerzaj�cy mo�liwo�ci
Pythona.

%description -l tr devel
Bu paket, Python ile geli�tirme yap�labilmesi i�in gerekli ba�l�k
dosyalar�n� ve kitapl�klar� i�erir.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python 
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Python'a 
Summary(tr):	Python belgeleri
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}

%description doc
This package contains documentation on the Python language and interpretor
as a mix of plain ASCII files and LaTeX sources.

%description -l de doc
Dieses Paket enth�lt Dokumentationen zu Python (Sprache und Interpreter) in
Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description -l fr doc
Ce paquetage contient la documentation sur le langage python et sur son
interpr�teur sous forme de fichiers ASCII et LaTeX.

%description -l pl doc
Oficjalna dokumentacja do Pythona. Zawiera przyk�adowe programy, narz�dzia
i dokumentacj�. Strony podr�cznika man znajduj� si� w g��wnym pakiecie. Ten
pakiet nie zawiera �r�de� dokumentacji napisanych w LaTeX'u, tylko gotowe
do wykorzystania pliki postscript'owe i HTML.

%description -l tr doc
Bu paket, Python dili ile ilgili belgeleri ve d�z ASCII dosyalar� ve LaTeX
kaynaklar�n�n bir kar���m� olan yorumlay�c�y� i�erir.

%package -n tkinter
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfl�che f�r Python
Summary(fr):	Interface graphique pour python.
Summary(pl):	Modu�y niskiego poziomu dla pakietu Python-tkinter
Summary(tr):	Python i�in grafik kullan�c� aray�z�
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}
Requires:	tcl >= 8.0.3 
Requires:	tk  >= 8.0.3
Requires:	tix >= 4.1.0.6

%description -n tkinter
This is the lowlevel C module that interfaces Tk and which is the basis for
the Tkinter, Python's OO interface to Tk, which is included in the package
python-tkinter.

The only reason this file is removed from python-tkinter, is to make it
more easy to replay _tkinter with a PIL (Python Imaging Libary) aware
version of it. Look at my PIL distribution.

%description -l de -n tkinter
Eine grafische Schnittstelle f�r Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description -l fr -n tkinter
Interface graphique pour Python, bas�e sur Tcl/Tk et utilis�e par beaucoup
des outils de configuration.

%description -l pl -n tkinter 
Ten pakiet zawiera modu�y w C, kt�re po�rednicz� w wywo�aniach pomi�dzy
samym Tk a modu�em Tkinter b�d�cym g��wnym interfejsem Tk dla Pythona.

Jedynym powodem wydzielenia tego pakietu jest u�atwienie wymiany go na PIL
(Python Imaging Library).

%description -l tr -n tkinter
Python i�in Tcl/Tk'ye dayal� ve pek �ok ayarlama arac� taraf�ndan
kullan�lan grafik bir aray�zd�r.

%prep
%setup -q -n Python-%{version} -a1
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f Doc/{ref,}/.cvsignore

%build
export POSIXLY_CORRECT=TRUE
cp -f %{SOURCE2} Modules

echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

cp Lib/lib-old/rand.py Lib

LDFLAGS="-s"; export LDFLAGS
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure \
	--with-threads 

make OPT="$RPM_OPT_FLAGS -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

make install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SCRIPTDIR=$RPM_BUILD_ROOT%{_libdir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	CONFINCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}
cp libpython1.5.a $RPM_BUILD_ROOT%{_libdir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/%{name}1.5/lib-dynload/*.so \
	$RPM_BUILD_ROOT%{_libdir}/%{name}1.5/lib-dynload/_tk* \
	$RPM_BUILD_ROOT%{_libdir}/libpython1.5.a

strip $RPM_BUILD_ROOT%{_bindir}/python1.5
rm -f $RPM_BUILD_ROOT%{_bindir}/python
ln -s python1.5 $RPM_BUILD_ROOT%{_bindir}/python
ln -s libpython1.5.a $RPM_BUILD_ROOT%{_libdir}/libpython.a

gzip -9nf README $RPM_BUILD_ROOT%{_mandir}/man1/* \
	Misc/{ACKS,BLURB.LUTZ,COPYRIGHT,NEWS,HYPE,README,HISTORY}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README.gz Misc/{ACKS,COPYRIGHT,NEWS,HISTORY}.gz

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/python1.5
%attr(-,root,root) %{_libdir}/python1.5/*.py

%dir %{_libdir}/python1.5/lib-dynload
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/arraymodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/binascii.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/bsddbmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/cPickle.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/cStringIO.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/cmathmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/cryptmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/cursesmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/dbmmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/errnomodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/fcntlmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/gdbmmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/grpmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/mathmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/md5module.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/newmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/nismodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/operator.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/parsermodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/pwdmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/readline.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/resource.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/rotormodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/selectmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/shamodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/socketmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/stropmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/structmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/syslogmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/termios.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/timemodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/timingmodule.so
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/zlibmodule.so

%{_libdir}/python1.5/lib-stdwin/*.py

%dir %{_libdir}/python1.5/plat-*
%attr(755,root,root) %{_libdir}/python1.5/plat-*/regen
%{_libdir}/python1.5/plat-*/*.py

%files devel
%defattr(644,root,root,755)

%dir %{_includedir}/python1.5
%{_includedir}/python1.5/*.h
%{_libdir}/libpython1.5.a
%{_libdir}/libpython.a

%files doc
%defattr(644,root,root,755)
%doc Misc/HYPE.gz Misc/README.gz Misc/cheatsheet Misc/BLURB* Doc

%files -n tkinter
%defattr(644,root,root,755)

%{_libdir}/python1.5/lib-tk
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/_tkinter.so
