
%define python_compile_opt ./python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[2])"
%define python_compile ./python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[2])"

%define pver 2.1
 
Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfläche
Summary(fr):	Langage de script de tés haut niveau avec interface X
Summary(pl):	Python - jêzyk obiektowy wysokiego poziomu
Summary(tr):	X arayüzlü, yüksek düzeyli, kabuk yorumlayýcý dili
Name:		python
Version:	%{pver}
Release:	2
License:	BeOpen Python License
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
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
BuildRequires:	XFree86-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.0.8-7
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tix-devel
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	zlib-devel
BuildRequires:	gmp-devel
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
Python enthält Module, Klassen, Exceptions, High-Level dynamische
Datentypen und dynamisches Typisieren. Python unterstützt Interfaces
zu vielen Systemaufrufen und Libraries, sowie verschiedene
Fenstersysteme (X11, Motif, Tk, Mac und MFC)

Programmierer können neue built-in-Module für Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache für Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses
Paket enthält die meisten Standard-Python-Module, und Module zum
Ansprechen von Tix (Tk-widget set) und RPM.

Dokumentationen zu Python sind in python-doc enthalten.

%description -l fr
Python est un langage de script interprété et orienté objet. Il gère
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles bibliothèques systèmes
avec du code C est simple, ce qui rend Python facile à utiliser dans
des configs personnalisées.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfaçage avec les widgets Tix pour Tk
et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
jêzykiem programowania. Jest modularny, obs³uguje wyj±tki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python ³±czy w
sobie du¿e mo¿liwo¶ci i przejrzyst± sk³adniê. Posiada interfejsy do
wielu wywo³añ systemowych i bibliotek, w tym równie¿ do ró¿nych
bibliotek okienkowych. Mo¿liwo¶ci jego mo¿na jeszcze rozszerzaæ
poprzez odpowiednie modu³y pisane w C lub C++. Python mo¿e byæ równie¿
u¿yty jako element aplikacji, którym potrzebny jest interpreter do
skryptów. I wreszcie, Python jest wieloplatformowy, dzia³a na wielu
odmianach UNIX'a, Mac'u oraz PC pod DOS'em, Windows, WindowsNT oraz
OS/2.

%description -l tr
Python, nesneye yönelik bir kabuk yorumlayýcýdýr. Nesnelerin,
sýnýflarýn, modüllerin ve aykýrý durumlarýn dinamik yüklenmelerine
destek verir. C koduyla birlikte kullanýmý son derece kolaydýr. Bu
paket, standart Python birimlerinin çoðunun yanýsýra Tk ve RPM için
arayüz birimlerini de içerir.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr):	Bibliothèques et en-têtes pour construire du code python
Summary(pl):	Pliki nag³ówkowe i biblioteki Python'a
Summary(tr):	Python ile geliþtirme yapmak için gerekli dosyalar
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This packages
contains the header files and libraries which are needed to do both of
these tasks.

%description -l de devel
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und läßt sich in andere Programme
integrieren. Dieses Paket enthält die Header-Dateien und Libraries,
die für beide Aufgaben erforderlich sind.

%description -l fr devel
L'interpréteur Python est relativement facile à étendre avec des
extensions chargées dynamiquement et à insérer dans d'autres
programmes. Ce paquetage contient les en-têtes et les bibliothèques
nécessaires à ces deux tâches.

%description -l pl devel
Wszystko co potrzebne, aby napisaæ w C/C++ modu³ rozszerzaj±cy
mo¿liwo¶ci Pythona. S± tu równie¿ wersje ¼ród³owe modu³ów ze standardowej
biblioteki.

%description -l tr devel
Bu paket, Python ile geliþtirme yapýlabilmesi için gerekli baþlýk
dosyalarýný ve kitaplýklarý içerir.

%package static
Summary:	Static python library
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name}-devel = %{version}

%description static
Static python library.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python 
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Python'a 
Summary(tr):	Python belgeleri
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description -l de doc
Dieses Paket enthält Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description -l fr doc
Ce paquetage contient la documentation sur le langage python et sur
son interpréteur sous forme de fichiers ASCII et LaTeX.

%description -l pl doc
Oficjalna dokumentacja do Pythona. Zawiera przyk³adowe programy,
narzêdzia i dokumentacjê. Strony podrêcznika man znajduj± siê w
g³ównym pakiecie. Ten pakiet nie zawiera ¼róde³ dokumentacji
napisanych w LaTeX'u, tylko gotowe do wykorzystania pliki
postscript'owe i HTML.

%description -l tr doc
Bu paket, Python dili ile ilgili belgeleri ve düz ASCII dosyalarý ve
LaTeX kaynaklarýnýn bir karýþýmý olan yorumlayýcýyý içerir.

%package -n tkinter
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfläche für Python
Summary(fr):	Interface graphique pour python.
Summary(pl):	Modu³y niskiego poziomu dla pakietu Python-tkinter
Summary(tr):	Python için grafik kullanýcý arayüzü
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
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
Eine grafische Schnittstelle für Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description -l fr -n tkinter
Interface graphique pour Python, basée sur Tcl/Tk et utilisée par
beaucoup des outils de configuration.

%description -l pl -n tkinter 
Ten pakiet zawiera modu³y w C, które po¶rednicz± w wywo³aniach
pomiêdzy samym Tk a modu³em Tkinter bêd±cym g³ównym interfejsem Tk dla
Pythona.

Jedynym powodem wydzielenia tego pakietu jest u³atwienie wymiany go na
PIL (Python Imaging Library).

%description -l tr -n tkinter
Python için Tcl/Tk'ye dayalý ve pek çok ayarlama aracý tarafýndan
kullanýlan grafik bir arayüzdür.

%package old
Summary:	Depreciated Python modules
Summary(pl):	Nieaktualne modu³y jêzyka Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python = %{version}

%description old
Install this package when one of your program written in Python
is old as Miss Universum of 1918, who only you want to see... ooops,
which only you want to run. 

%description -l pl old
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich programów napisanych
w jêzyku Python jest tak stary jak Miss Universum z roku 1918, któr±
tylko ty chcesz zobaczyæ... przepraszam, który tylko ty chcesz uruchomiæ.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

install libpython%{pver}.a $RPM_BUILD_ROOT%{_libdir}

%python_compile $RPM_BUILD_ROOT%{_libdir}/python%{pver} %{_libdir}/python%{pver}
%python_compile_opt $RPM_BUILD_ROOT%{_libdir}/python%{pver} %{_libdir}/python%{pver}

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{pver}
ln -sf libpython%{pver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a

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

%dir %{_libdir}/python%{pver}
%{_libdir}/python%{pver}/*.py?
 
%dir %{_libdir}/python%{pver}/lib-dynload
%attr(755,root,root) %{_libdir}/python%{pver}/lib-dynload/[a-z]*.so
%attr(755,root,root) %{_libdir}/python%{pver}/lib-dynload/_te*.so
%attr(755,root,root) %{_libdir}/python%{pver}/lib-dynload/_[a-su-z]*.so

%dir %{_libdir}/python%{pver}/plat-*
%attr(755,root,root) %{_libdir}/python%{pver}/plat-*/regen
%{_libdir}/python%{pver}/plat-*/*.py?

%dir %{_libdir}/python%{pver}/curses
%{_libdir}/python%{pver}/curses/*.py?

%dir %{_libdir}/python%{pver}/distutils
%{_libdir}/python%{pver}/distutils/*.py?

%dir %{_libdir}/python%{pver}/distutils/command
%{_libdir}/python%{pver}/distutils/command/*.py?

%dir %{_libdir}/python%{pver}/encodings
%{_libdir}/python%{pver}/encodings/*.py?

%dir %{_libdir}/python%{pver}/xml
%{_libdir}/python%{pver}/xml/*.py?

%dir %{_libdir}/python%{pver}/xml/parsers
%{_libdir}/python%{pver}/xml/parsers/*.py?

%dir %{_libdir}/python%{pver}/xml/sax
%{_libdir}/python%{pver}/xml/sax/*.py?

%dir %{_libdir}/python%{pver}/xml/dom
%{_libdir}/python%{pver}/xml/dom/*.py?

%files devel
%defattr(644,root,root,755)
%doc *.gz Misc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/python%{pver}
%{_includedir}/python%{pver}/*.h
%attr(-,root,root) %{_libdir}/python%{pver}/*.py
%{_libdir}/python%{pver}/plat-*/*.py
%{_libdir}/python%{pver}/curses/*.py
%{_libdir}/python%{pver}/distutils/*.py
%{_libdir}/python%{pver}/distutils/command/*.py
%{_libdir}/python%{pver}/xml/*.py
%{_libdir}/python%{pver}/xml/parsers/*.py
%{_libdir}/python%{pver}/xml/sax/*.py
%{_libdir}/python%{pver}/xml/dom/*.py
%{_libdir}/python%{pver}/encodings/*.py

%dir %{_libdir}/python%{pver}/config
%attr(755,root,root) %{_libdir}/python%{pver}/config/makesetup
%attr(755,root,root) %{_libdir}/python%{pver}/config/install-sh
%{_libdir}/python%{pver}/config/Makefile
%{_libdir}/python%{pver}/config/Makefile.pre.in
%{_libdir}/python%{pver}/config/Setup
%{_libdir}/python%{pver}/config/Setup.config
%{_libdir}/python%{pver}/config/Setup.local
%{_libdir}/python%{pver}/config/config.c
%{_libdir}/python%{pver}/config/config.c.in
%{_libdir}/python%{pver}/config/python.o

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files doc
%defattr(644,root,root,755)
%doc html-doc/*
%dir %{_libdir}/python%{pver}/test
%attr(-,root,root) %{_libdir}/python%{pver}/test/*

%files -n tkinter
%defattr(644,root,root,755)

%{_libdir}/python%{pver}/lib-tk
%attr(755,root,root) %{_libdir}/python%{pver}/lib-dynload/_tkinter.so

%files old
%defattr(644,root,root,755)

%dir %{_libdir}/python%{pver}/lib-old
%{_libdir}/python%{pver}/lib-old/*.py?
