%define py_ver         2.2
%define py_prefix      %{_prefix}
%define py_libdir      %{py_prefix}/lib/python%{py_ver}
%define py_incdir      %{_includedir}/python%{py_ver}
%define py_sitedir     %{py_libdir}/site-packages
%define py_dyndir      %{py_libdir}/lib-dynload
%define py_comp        ./python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"
%define py_ocomp       ./python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"

Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfläche
Summary(es):	Lenguaje script de alto nivel con interface X
Summary(fr):	Langage de script de tés haut niveau avec interface X
Summary(pl):	Python - jêzyk obiektowy wysokiego poziomu
Summary(pt_BR):	Linguagem de programação interpretada, orientada a objeto de alto nível
Summary(tr):	X arayüzlü, yüksek düzeyli, kabuk yorumlayýcý dili
Name:		python
Version:	%{py_ver}.1
Release:	2
License:	PSF
Group:		Applications
URL:		http://www.python.org/
Source0:	http://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
Source1:	http://www.python.org/ftp/python/doc/%{version}/html-%{version}.tar.bz2
Source2:	%{name}-setup.dist
Patch0:		%{name}-shared-lib.patch
Patch1:		%{name}-readline.patch
Patch2:		%{name}-%{name}path.patch
Patch3:		%{name}-ac25x.patch
Patch4:		%{name}-default_encoding.patch
Patch5:		%{name}-no_ndbm.patch
Patch6:		%{name}-ac_fixes.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	db3-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.0.8-7
BuildRequires:	gmp-devel => 4.0
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.6b
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tix-devel
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	%{name} = %{py_ver}
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

%description -l es
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga dinámica de objetos, clases, módulos y
excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca a
través de código C, tornando Python fácil de usar en ambientes
articulares/ personalizados. Este paquete Python incluye la mayoría de
los módulos padrón Python, junto con módulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

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
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

%description -l pt_BR
Python é uma linguagem de scripts interpretada orientada a objetos.
Contém suporte para carga dinâmica de objetos, classes, módulos e
exceções. Adicionar interfaces para novos sistemas de biblioteca
através de código C é simples, tornando Python fácil de usar em
ambientes particulares/personalizados.

Este pacote Python inclui a maioria do módulos padrão Python, junto
com módulos para interfaceamento para o conjunto de componentes Tix
para Tk e RPM.

%description -l tr
Python, nesneye yönelik bir kabuk yorumlayýcýdýr. Nesnelerin,
sýnýflarýn, modüllerin ve aykýrý durumlarýn dinamik yüklenmelerine
destek verir. C koduyla birlikte kullanýmý son derece kolaydýr. Bu
paket, standart Python birimlerinin çoðunun yanýsýra Tk ve RPM için
arayüz birimlerini de içerir.

%package libs
Summary:	Python library
Summary(pl):	Biblioteka jêzyka Python
Group:		Libraries/Python
Provides:	%{name}-libs = %{py_ver}

%description libs
Python library.

%description libs -l pl
Biblioteka jêzyka Python.

%package modules
Summary:	Python modules
Summary(pl):	Modu³y jêzyka Python
Group:		Libraries/Python
Provides:	%{name}-modules = %{py_ver}
Requires:	%{name} = %{version}

%description modules
Python modules.

%description modules -l pl
Modu³y jêzyka Python.

%package pydoc
Summary:	Python interactive module documentation access support
Summary(pl):	Interaktywne korzystanie z dokumentacji modu³ów jêzyka Python
Group:		Applications
Requires:	%{name}-modules = %{version}

%description pydoc
Python interactive module documentation access support.

%description pydoc -l pl
Interaktywne korzystanie z dokumentacji modu³ów jêzyka Python.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(es):	Bibliotecas y archivos de inclusión para construir programas en python
Summary(fr):	Bibliothèques et en-têtes pour construire du code python
Summary(pl):	Pliki nag³ówkowe i biblioteki Pythona
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para o Python
Summary(tr):	Python ile geliþtirme yapmak için gerekli dosyalar
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This packages
contains the header files and libraries which are needed to do both of
these tasks.

%description devel -l de
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und läßt sich in andere Programme
integrieren. Dieses Paket enthält die Header-Dateien und Libraries,
die für beide Aufgaben erforderlich sind.

%description devel -l es
El interpretador Python permite incluir con facilidad extensiones
cargadas dinámicamente. Python es también fácil de ser empotrado en
otros programas. Este paquete contiene los archivos de inclusión y
bibliotecas necesarios para estas dos tareas.

%description devel -l fr
L'interpréteur Python est relativement facile à étendre avec des
extensions chargées dynamiquement et à insérer dans d'autres
programmes. Ce paquetage contient les en-têtes et les bibliothèques
nécessaires à ces deux tâches.

%description devel -l pl
Wszystko co potrzebne, aby napisaæ w C/C++ modu³ rozszerzaj±cy
mo¿liwo¶ci Pythona. S± tu równie¿ wersje ¼ród³owe modu³ów ze
standardowej biblioteki.

%description devel -l pt_BR
O interpretador Python permite incluir com facilidade extensões
carregadas dinamicamente. Python é também fácil de ser embutido em
outros programas. Este pacote contém os arquivos de inclusão e
bibliotecas necessários para estas duas tarefas.

%description devel -l tr
Bu paket, Python ile geliþtirme yapýlabilmesi için gerekli baþlýk
dosyalarýný ve kitaplýklarý içerir.

%package devel-src
Summary:	Python module sources
Summary(pl):	Pliki ¼ród³owe modu³ów Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{version}

%description devel-src
Python module sources.

%description devel-src -l pl
Pliki ¼ród³owe modu³ów Pythona.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Provides:	%{name}-static = %{py_ver}
Requires:	%{name}-devel = %{version}

%description static
Static python library.

%description static -l pl
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python
Summary(es):	Documentación para Python
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Pythona
Summary(pt_BR):	Documentação para a linguagem de programação Python.
Summary(tr):	Python belgeleri
Group:		Documentation
Requires:	%{name} = %{version}
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description doc -l de
Dieses Paket enthält Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description doc -l es
Documentación para Python. Contiene archivos en texto y PostScript.

%description doc -l fr
Ce paquetage contient la documentation sur le langage python et sur
son interpréteur sous forme de fichiers ASCII et LaTeX.

%description doc -l pl
Oficjalna dokumentacja do Pythona. Zawiera przyk³adowe programy,
narzêdzia i dokumentacjê. Strony podrêcznika man znajduj± siê w
g³ównym pakiecie. Ten pakiet nie zawiera ¼róde³ dokumentacji
napisanych w LaTeX'u, tylko gotowe do wykorzystania pliki
postscript'owe i HTML.

%description doc -l pt_BR
O pacote python-doc contém documentação para a linguagem de
programação e para o interpretador Python. Fornecida em arquivos texto
e Postcript.

%description doc -l tr
Bu paket, Python dili ile ilgili belgeleri ve düz ASCII dosyalarý ve
LaTeX kaynaklarýnýn bir karýþýmý olan yorumlayýcýyý içerir.

%package without-thread
Summary:	Python without threads
Summary(pl):	Pyton bez w±tków
Group:		Libraries/Python
Provides:	%{name}-without-thread = %{py_ver}
Requires:	%{name} = %{version}
Obsoletes:	python-without-thread

%description without-thread
This package is rather needed for apache-mod_python module. Other ways
of use are unknown.

%description without-thread -l pl
Pyton bez w±tków jest w³a¶ciwie potrzebny tylko modu³owi
apache-mod_python, bo apache nie ich na razie nie wspiera.

%package -n tkinter
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfläche für Python
Summary(es):	Interface GUI para Phyton
Summary(fr):	Interface graphique pour python.
Summary(pl):	Modu³y niskiego poziomu dla pakietu Python-tkinter
Summary(pt_BR):	Interface GUI para Phyton
Summary(tr):	Python için grafik kullanýcý arayüzü
Group:		Libraries/Python
Requires:	%{name}-modules = %{version}
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

%description -n tkinter -l de
Eine grafische Schnittstelle für Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description -n tkinter -l es
Una interface gráfica para Python, basada en Tcl/Tk, y usada por
muchas herramientas de configuración.

%description -n tkinter -l fr
Interface graphique pour Python, basée sur Tcl/Tk et utilisée par
beaucoup des outils de configuration.

%description -n tkinter -l pl
Ten pakiet zawiera modu³y w C, które po¶rednicz± w wywo³aniach
pomiêdzy samym Tk a modu³em Tkinter bêd±cym g³ównym interfejsem Tk dla
Pythona.

Jedynym powodem wydzielenia tego pakietu jest u³atwienie wymiany go na
PIL (Python Imaging Library).

%description -n tkinter -l pt_BR
Uma interface gráfica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configuração.

%description -n tkinter -l tr
Python için Tcl/Tk'ye dayalý ve pek çok ayarlama aracý tarafýndan
kullanýlan grafik bir arayüzdür.

%package old
Summary:	Depreciated Python modules
Summary(pl):	Nieaktualne modu³y jêzyka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{version}

%description old
Install this package when one of your program written in Python is old
as Miss Universum of 1918, who only you want to see... ooops, which
only you want to run.

%description old -l pl
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich programów napisanych
w jêzyku Python jest tak stary jak Miss Universum z roku 1918, któr±
tylko ty chcesz zobaczyæ... przepraszam, który tylko ty chcesz
uruchomiæ.

%package examples
Summary:	Example programs in Python
Summary(pl):	Przyk³adowe programy w Pythonie
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{version}
Obsoletes:	python-tools

%description examples
Example programs in Python.

%description examples -l pl
Przyk³adowe programy w Pythonie.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

install -d html-doc
tar -xf %{SOURCE1} --use=bzip2 -C html-doc

install %{SOURCE2} Modules/Setup

%build
echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

autoconf

POSIXLY_CORRECT=TRUE; export POSIXLY_CORRECT

CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/db3"; export CPPFLAGS
%configure \
	--with-threads

%{__make} OPT="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

LD_LIBRARY_PATH=$(pwd)
export LD_LIBRARY_PATH
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SCRIPTDIR=$RPM_BUILD_ROOT%{_libdir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	CONFINCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

install libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}

%py_comp $RPM_BUILD_ROOT%{py_libdir}
%py_ocomp $RPM_BUILD_ROOT%{py_libdir}

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a

install -d $RPM_BUILD_ROOT%{_examplesdir}/python
cp -ar Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/python

install Tools/scripts/pydoc $RPM_BUILD_ROOT%{_bindir}

gzip -9nf Misc/{ACKS,NEWS,README}

echo "%defattr(644,root,root,755)" > modules.filelist

find $RPM_BUILD_ROOT%{py_libdir} \
	-type f \
	-maxdepth 1 \
	-printf %{py_libdir}/%f\\n \
	| grep '\.py[co]$' \
	| grep -v -e 'UserDict\.py[oc]$'\
	| grep -v -e 'codecs\.py[oc]$' \
	| grep -v -e 'locale\.py[oc]$' \
	| grep -v -e 'posixpath\.py[oc]$' \
	| grep -v -e 'pydoc\.py[oc]$' \
	| grep -v -e 'site\.py[oc]$' \
	| grep -v -e 'stat\.py[oc]$' \
	| grep -v -e 'os\.py[oc]$' \
	| grep -v -e 'encodings\/.*\.py[oc]$' >> modules.filelist

find $RPM_BUILD_ROOT%{py_dyndir} \
	-type f \
	-maxdepth 1 \
	-printf "%%%%attr(755,root,root) %{py_dyndir}/%f\\n" \
	| grep '\.so$' \
	| grep -v -e 'codecsmodule\.so$' \
	| grep -v -e 'readline\.so$' \
	| grep -v -e 'structmodule\.so$' \
	| grep -v -e '_tkinter\.so$' >> modules.filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/*

# readline support for python binary
%attr(755,root,root) %{py_dyndir}/readline.so

%files modules -f modules.filelist
%defattr(644,root,root,755)

%dir %{py_libdir}/plat-*
%attr(755,root,root) %{py_libdir}/plat-*/regen
%{py_libdir}/plat-*/*.py?

%dir %{py_libdir}/compiler
%{py_libdir}/compiler/*.py?

%dir %{py_libdir}/curses
%{py_libdir}/curses/*.py?

%dir %{py_libdir}/distutils
%{py_libdir}/distutils/*.py?

%dir %{py_libdir}/distutils/command
%{py_libdir}/distutils/command/*.py?

%dir %{py_libdir}/email
%{py_libdir}/email/*.py?

%dir %{py_libdir}/hotshot
%{py_libdir}/hotshot/*.py?

%dir %{py_libdir}/xml
%{py_libdir}/xml/*.py?

%dir %{py_libdir}/xml/parsers
%{py_libdir}/xml/parsers/*.py?

%dir %{py_libdir}/xml/sax
%{py_libdir}/xml/sax/*.py?

%dir %{py_libdir}/xml/dom
%{py_libdir}/xml/dom/*.py?

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*so.*

%dir %{py_dyndir}
%dir %{py_libdir}
%dir %{py_sitedir}

# required shared modules by python library
%attr(755,root,root) %{py_dyndir}/_codecsmodule.so
%attr(755,root,root) %{py_dyndir}/structmodule.so

# required modules by python library
%{py_libdir}/UserDict.py?
%{py_libdir}/codecs.py?
%{py_libdir}/locale.py?
%{py_libdir}/posixpath.py?
%{py_libdir}/site.py?
%{py_libdir}/stat.py?
%{py_libdir}/os.py?

# required encodings by python library
%dir %{py_libdir}/encodings
%{py_libdir}/encodings/*.py?

%files pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_libdir}/pydoc.py?

%files devel
%defattr(644,root,root,755)
%doc Misc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{py_incdir}
%{py_incdir}/*.h

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

%files devel-src
%defattr(644,root,root,755)
%attr(-,root,root) %{py_libdir}/*.py
%{py_libdir}/plat-*/*.py
%{py_libdir}/compiler/*.py
%{py_libdir}/curses/*.py
%{py_libdir}/distutils/*.py
%{py_libdir}/distutils/command/*.py
%{py_libdir}/email/*.py
%{py_libdir}/hotshot/*.py
%{py_libdir}/xml/*.py
%{py_libdir}/xml/parsers/*.py
%{py_libdir}/xml/sax/*.py
%{py_libdir}/xml/dom/*.py
%{py_libdir}/encodings/*.py

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
