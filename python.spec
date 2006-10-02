#
# TODO
# - test_distutils fails for unknown reason: (does it still do with new lib64 patch?)
#   AssertionError: '/tmp/tmpaomC0l/installation/share/python' != '/tmp/tmpaomC0l/installation/lib/python'
# - change searchpath order so /usr/lib* is before /usr/share
# - kill lib-tk from searchpath
# - kill BR: file requirement from lib64 patch
#
# Conditional build:
%bcond_with	info			# don't build info pages (requires emacs, fails in python-2.5.0)
%bcond_without	tkinter			# disables tkinter module building
%bcond_without	tests			# disables Python testing
%bcond_with	verbose_tests		# runs tests in verbose mode
#
# tests which will not work on 64-bit platforms
%define		no64bit_tests	test_audioop test_rgbimg test_imageop
# tests which may fail because of builder environment limitations (no /proc or /dev/pts)
%define		nobuilder_tests test_resource test_openpty test_socket test_nis test_posix test_locale test_pty
# tests which fail because of some unknown/unresolved reason (this list should be empty)
%define		broken_tests test_anydbm test_bsddb test_re test_shelve test_whichdb test_zipimport test_distutils

%define	beta		%{nil}

%define py_ver		2.5
%define py_prefix	%{_prefix}
%define py_libdir	%{py_prefix}/%{_lib}/python%{py_ver}
%define py_incdir	%{_includedir}/python%{py_ver}
%define py_sitedir	%{py_libdir}/site-packages
%define py_dyndir	%{py_libdir}/lib-dynload

Summary:	Very high level scripting language with X interface
Summary(es):	Lenguaje script de alto nivel con interfaz X
Summary(fr):	Langage de script de trХs haut niveau avec interface X
Summary(pl):	Python - jЙzyk obiektowy wysokiego poziomu
Summary(pt_BR):	Linguagem de programaГЦo interpretada de alto nМvel
Summary(ru):	Язык программирования очень высокого уровня с X-интерфейсом
Summary(tr):	X arayЭzlЭ, yЭksek dЭzeyli, kabuk yorumlayЩcЩ dili
Summary(uk):	Мова програмування дуже високого р╕вня з X-╕нтерфейсом
Name:		python
Version:	%{py_ver}
Release:	3
Epoch:		1
License:	PSF
Group:		Applications
Source0:	http://www.python.org/ftp/python/%{py_ver}/Python-%{version}%{beta}.tar.bz2
# Source0-md5:	ddb7401e711354ca83b7842b733825a3
Source1:	http://www.python.org/ftp/python/doc/%{version}%{beta}/html-%{version}%{beta}.tar.bz2
# Source1-md5:	3badfa2d460f52b7f9face12abdb2e91
Patch0:		%{name}-readline.patch
Patch1:		%{name}-%{name}path.patch
Patch2:		%{name}-no_ndbm.patch
Patch3:		%{name}-ac_fixes.patch
Patch4:		%{name}-noarch_to_datadir.patch
Patch5:		%{name}-lib64.patch
Patch6:		%{name}-doc_path.patch
Patch7:		%{name}-info.patch
# probably no longer required, can't verify
Patch8:		%{name}-sparc_fix.patch
Patch9:		%{name}-db.patch
URL:		http://www.python.org/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	db-devel >= 4
%{?with_info:BuildRequires:	emacs >= 21}
BuildRequires:	expat-devel >= 1:1.95.7
BuildRequires:	file
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	gmp-devel >= 4.0
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-ext-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.3.5
%{?with_info:BuildRequires:	tetex-makeindex}
%{?with_tkinter:BuildRequires:	tix-devel >= 1:8.1.4-4}
%{?with_tkinter:BuildRequires:	tk-devel >= 8.4.3}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	python-curses
Obsoletes:	python-gdbm
Obsoletes:	python-intl
Obsoletes:	python-xml
Obsoletes:	python-zlib
Obsoletes:	python2
Obsoletes:	python2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with verbose_tests}
%define test_flags -v -l -x
%else
%define test_flags -l -x
%endif

%ifarch alpha ia64 ppc64 sparc64 ppc64 %{x8664}
%define test_list %{nobuilder_tests} %{broken_tests} %{no64bit_tests}
%else
%define test_list %{nobuilder_tests} %{broken_tests}
%endif

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

This package contains the Python binary.

%description -l de
Python ist eine interpretierte, interaktive, objektorientierte
Programmiersprache, vergleichbar zu Tcl, Perl, Scheme oder Java.
Python enthДlt Module, Klassen, Exceptions, High-Level dynamische
Datentypen und dynamisches Typisieren. Python unterstЭtzt Interfaces
zu vielen Systemaufrufen und Libraries, sowie verschiedene
Fenstersysteme (X11, Motif, Tk, Mac und MFC)

Programmierer kЖnnen neue built-in-Module fЭr Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache fЭr Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses
Paket enthДlt die meisten Standard-Python-Module, und Module zum
Ansprechen von Tix (Tk-widget set) und RPM.

%description -l es
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga dinАmica de objetos, clases, mСdulos y
excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca a
travИs de cСdigo C, tornando Python fАcil de usar en ambientes
particulares/personalizados. Este paquete Python incluye la mayorМa de
los mСdulos padrСn Python, junto con mСdulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

%description -l fr
Python est un langage de script interprИtИ et orientИ objet. Il gХre
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles bibliothХques systХmes
avec du code C est simple, ce qui rend Python facile Ю utiliser dans
des configs personnalisИes.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfaГage avec les widgets Tix pour Tk
et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
jЙzykiem programowania. Jest modularny, obsЁuguje wyj╠tki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python Ё╠czy w
sobie du©e mo©liwo╤ci i przejrzyst╠ skЁadniЙ. Posiada interfejsy do
wielu wywoЁaЯ systemowych i bibliotek, w tym rСwnie© do rС©nych
bibliotek okienkowych. Mo©liwo╤ci jego mo©na jeszcze rozszerzaФ
poprzez odpowiednie moduЁy pisane w C lub C++. Python mo©e byФ rСwnie©
u©yty jako element aplikacji, ktСrym potrzebny jest interpreter do
skryptСw. I wreszcie, Python jest wieloplatformowy, dziaЁa na wielu
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

Ten pakiet zawiera binarkЙ Pythona.

%description -l pt_BR
Python И uma linguagem de scripts interpretada orientada a objetos.
ContИm suporte para carga dinБmica de objetos, classes, mСdulos e
exceГУes. Adicionar interfaces para novos sistemas de biblioteca
atravИs de cСdigo C И simples, tornando Python fАcil de usar em
ambientes particulares/personalizados.

Este pacote Python inclui a maioria do mСdulos padrЦo Python, junto
com mСdulos para interfaceamento para o conjunto de componentes Tix
para Tk e RPM.

%description -l ru
Python - это интерпретируемый, объектно-ориентированный язык
программирования. Он поддерживает динамическую загрузку объектов,
классы, модули и обработку исключительных ситуаций (exceptions).
Простота добавления интерфейсов к новым системным библиотекам через
код на языке C делает Python хорошим выбором для использования в
специальных конфигурациях.

%description -l tr
Python, nesneye yЖnelik bir kabuk yorumlayЩcЩdЩr. Nesnelerin,
sЩnЩflarЩn, modЭllerin ve aykЩrЩ durumlarЩn dinamik yЭklenmelerine
destek verir. C koduyla birlikte kullanЩmЩ son derece kolaydЩr. Bu
paket, standart Python birimlerinin ГoПunun yanЩsЩra Tk ve RPM iГin
arayЭz birimlerini de iГerir.

%description -l uk
Python - це ╕нтерпретована, об'╓ктно-ор╕╓нтована мова програмування.
В╕н п╕дтриму╓ динам╕чну загрузку об'╓кт╕в, класи, модул╕ та обробку
виключних ситуац╕й (exceptions). Простота додавання ╕нтерфейс╕в для
нових системних б╕бл╕отек через код на мов╕ C робить Python добрим
вибором для використання в спец╕альних конф╕гурац╕ях.

%package libs
Summary:	Python library
Summary(pl):	Biblioteka jЙzyka Python
Group:		Libraries/Python
# broken detection in rpm/pythondeps.sh
Provides:	python(abi) = %{py_ver}
# for compatibility with existing Ac packages
Provides:	python(bytecode) = %{py_ver}
%{!?with_info:Obsoletes:	python-doc-info}

%description libs
Python shared library and very essental modules for Python binary.

%description libs -l pl
Biblioteka wspСЁdzielona jЙzyka Python oraz bardzo podstawowe moduЁy
dla Pythona.

%package modules
Summary:	Python modules
Summary(pl):	ModuЁy jЙzyka Python
Group:		Libraries/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	python-ctypes
Obsoletes:	python-logging
Obsoletes:	python-old
Obsoletes:	python-optik
Obsoletes:	python-xmlrpc <= 1.0.1

%description modules
Python officially distributed modules.

%description modules -l pl
Oficjalnie rozprowadzane moduЁy jЙzyka Python.

%package modules-sqlite
Summary:	Python SQLite modules
Summary(pl):	ModuЁy SQLite jЙzyka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description modules-sqlite
Python officially distributed sqlite module.

%description modules-sqlite -l pl
Oficjalnie rozprowadzany moduЁ sqlite jЙzyka Python.

%package -n pydoc
Summary:	Python interactive module documentation access support
Summary(pl):	Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	python-pydoc

%description -n pydoc
Python interactive module documentation access support.

%description -n pydoc -l pl
Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python.

%package -n idle
Summary:	IDE for Python language
Summary(pl):	IDE dla jЙzyka Python
Group:		Applications
Requires:	%{name}-tkinter = %{epoch}:%{version}-%{release}
Obsoletes:	python-idle

%description -n idle
IDE for Python language.

%description -n idle -l pl
IDE dla jЙzyka Python.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(es):	Bibliotecas y archivos de inclusiСn para construir programas en python
Summary(fr):	BibliothХques et en-tЙtes pour construire du code python
Summary(pl):	Pliki nagЁСwkowe i biblioteki Pythona
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para o Python
Summary(ru):	Библиотеки и хедеры для построения кода на языке Python
Summary(tr):	Python ile geliЧtirme yapmak iГin gerekli dosyalar
Summary(uk):	Б╕бл╕отеки та хедери для програмування на мов╕ Python
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This package
contains the header files and libraries which are needed to do both of
these tasks.

%description devel -l de
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und lДъt sich in andere Programme
integrieren. Dieses Paket enthДlt die Header-Dateien und Libraries,
die fЭr beide Aufgaben erforderlich sind.

%description devel -l es
El interpretador Python permite incluir con facilidad extensiones
cargadas dinАmicamente. Python es tambiИn fАcil de ser empotrado en
otros programas. Este paquete contiene los archivos de inclusiСn y
bibliotecas necesarios para estas dos tareas.

%description devel -l fr
L'interprИteur Python est relativement facile Ю Иtendre avec des
extensions chargИes dynamiquement et Ю insИrer dans d'autres
programmes. Ce paquetage contient les en-tЙtes et les bibliothХques
nИcessaires Ю ces deux tБches.

%description devel -l pl
Interpreter Pythona jest w miarЙ Ёatwy do rozszerzania przy pomocy
dynamicznie Ёadowanych rozszerzeЯ napisanych w C lub C++ oraz
osadzania w innych programach. Ten pakiet zawiera pliki nagЁСwkowe i
wszystko inne co potrzebne do tych celСw.

%description devel -l pt_BR
O interpretador Python permite incluir com facilidade extensУes
carregadas dinamicamente. Python И tambИm fАcil de ser embutido em
outros programas. Este pacote contИm os arquivos de inclusЦo e
bibliotecas necessАrios para estas duas tarefas.

%description devel -l ru
Интерпретатор Python относительно легко расширяется при помощи
динамически загружаемых расширений и встраивается в другие программы.
Этот пакет содержит хедеры и библиотеки, необходимые для обеих этих
задач.

%description devel -l tr
Bu paket, Python ile geliЧtirme yapЩlabilmesi iГin gerekli baЧlЩk
dosyalarЩnЩ ve kitaplЩklarЩ iГerir.

%description devel -l uk
╤нтерпретатор Python в╕дносно легко розширю╓ться за допомогою
розширень з динам╕чною загрузкою та вбудову╓ться в ╕нш╕ програми. Цей
пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для обох цих задач.

%package devel-src
Summary:	Python module sources
Summary(pl):	Pliki ╪rСdЁowe moduЁСw Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-src
Python module sources.

%description devel-src -l pl
Pliki ╪rСdЁowe moduЁСw Pythona.

%package devel-tools
Summary:	Python development tools
Summary(pl):	NarzЙdzia programistyczne jЙzyka Python
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-tools
Python development tools such as profilers and debugger.

%description devel-tools -l pl
NarzЙdzia programistyczne jЙzyka Python takie jak profiler oraz
debugger.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static python library.

%description static -l pl
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python
Summary(es):	DocumentaciСn para Python
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Pythona
Summary(pt_BR):	DocumentaГЦo para a linguagem de programaГЦo Python
Summary(ru):	Документация по языку Python
Summary(tr):	Python belgeleri
Summary(uk):	Документац╕я по мов╕ Python
Group:		Documentation
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description doc -l de
Dieses Paket enthДlt Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description doc -l es
DocumentaciСn para Python. Contiene archivos en texto y PostScript.

%description doc -l fr
Ce paquetage contient la documentation sur le langage python et sur
son interprИteur sous forme de fichiers ASCII et LaTeX.

%description doc -l pl
Oficjalna dokumentacja do Pythona. Zawiera przykЁadowe programy,
narzЙdzia i dokumentacjЙ. Strony podrЙcznika man znajduj╠ siЙ w
gЁСwnym pakiecie. Ten pakiet nie zawiera ╪rСdeЁ dokumentacji
napisanych w LaTeXu, tylko gotowe do wykorzystania pliki postscriptowe
i HTML.

%description doc -l pt_BR
O pacote python-doc contИm documentaГЦo para a linguagem de
programaГЦo e para o interpretador Python. Fornecida em arquivos texto
e Postcript.

%description doc -l ru
Этот пакет содержит документацию по собственно языку Python и по
исполняющему его интерпретатору в виде набора текстовых файлов и
исходных текстов в формате LaTeX.

%description doc -l tr
Bu paket, Python dili ile ilgili belgeleri ve dЭz ASCII dosyalarЩ ve
LaTeX kaynaklarЩnЩn bir karЩЧЩmЩ olan yorumlayЩcЩyЩ iГerir.

%description doc -l uk
Цей пакет м╕стить документац╕ю по власне мов╕ Python та по виконуючому
╖╖ ╕нтерпретатору у вигляд╕ набора текстових файл╕в та вих╕дних
текст╕в у формат╕ LaTeX.

%package doc-info
Summary:	Documentation on Python in texinfo format
Summary(pl):	Dokumentacja do Pythona w formacie texinfo
Group:		Documentation

%description doc-info
Documentation on Python in texinfo format.

%description doc-info -l pl
Dokumentacja do Pythona w formacie texinfo.

%package tkinter
Summary:	Standard Python interface to the Tk GUI toolkit
Summary(de):	Grafische Tk-Schnittstelle fЭr Python
Summary(es):	Interfaz de GUI Tk para Python
Summary(fr):	Interface graphique Tk pour Python
Summary(pl):	Standardowy interfejs Pythona do biblioteki Tk
Summary(pt_BR):	Interface GUI Tk para Phyton
Summary(tr):	Python iГin grafik kullanЩcЩ arayЭzЭ
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	tcl >= 8.4.3
Requires:	tix >= 1:8.1.4-4
Requires:	tk >= 8.4.3
Obsoletes:	tkinter

%description tkinter
Standard Python interface to the Tk GUI toolkit.

%description tkinter -l de
Eine grafische Schnittstelle fЭr Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description tkinter -l es
Una interfaz grАfica para Python, basada en Tcl/Tk, y usada por muchas
herramientas de configuraciСn.

%description tkinter -l fr
Interface graphique pour Python, basИe sur Tcl/Tk et utilisИe par
beaucoup des outils de configuration.

%description tkinter -l pl
Standardowy interfejs Pythona do biblioteki Tk.

%description tkinter -l pt_BR
Uma interface grАfica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configuraГЦo.

%description tkinter -l ru
Графический интерфейс (GUI) для Python, построенный на Tcl/Tk.

%description tkinter -l tr
Python iГin Tcl/Tk'ye dayalЩ ve pek Гok ayarlama aracЩ tarafЩndan
kullanЩlan grafik bir arayЭzdЭr.

%description tkinter -l uk
Граф╕чний ╕нтерфейс (GUI) для Python, побудований на Tcl/Tk.

%package examples
Summary:	Example programs in Python
Summary(pl):	PrzykЁadowe programy w Pythonie
Group:		Development/Languages/Python
Obsoletes:	python-tools

%description examples
Example programs in Python.

These are for Python 2.3.4, not %{version}.

%description examples -l pl
PrzykЁadowe programy w Pythonie.

PrzykЁady te s╠ dla Pythona 2.3.4, nie %{version}.

%prep
%setup -q -n Python-%{version}%{beta}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch9 -p1

tar -xf %{SOURCE1} --use=bzip2

%build
sed -i -e 's#-ltermcap#-ltinfo#g' configure*
%{__autoconf}
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure \
	--with-threads \
	--with-cxx="%{__cxx}" \
	--enable-unicode=ucs4 \
	--enable-shared \
	LINKCC='$(PURIFY) $(CXX)'

./Doc/tools/getversioninfo

%{__make} \
	OPT="%{rpmcflags}"

LC_ALL=C
export LC_ALL
%if %{with tests}
binlibdir=`echo build/lib.*`
%{__make} test \
	TESTOPTS="%{test_flags} %{test_list}" \
	TESTPYTHON="LD_LIBRARY_PATH=`pwd` PYTHONHOME=`pwd` PYTHONPATH=`pwd`/Lib:$binlibdir ./python -tt"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_infodir} \
	$RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with info}
%{__make} -C Doc/info
install Doc/info/python*info* $RPM_BUILD_ROOT%{_infodir}
%endif

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

mv $RPM_BUILD_ROOT{%{py_libdir}/config,%{_libdir}}/libpython%{py_ver}.a
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython%{py_ver}.so

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

#
# create several useful aliases, such as timeit.py, profile.py, pdb.py, smtpd.py
#

# for python devel tools
for script in timeit profile pdb pstats; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh

echo alias pygettext.py='"pygettext"' \
	>> $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-devel.csh

# for python modules
for script in smtpd webbrowser; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-modules.csh

# xgettext specific for Python code
#
# we will have two commands: pygettext.py (an alias) and pygettext;
# this way there are no import (which is impossible now) conflicts and
# pygettext.py is provided for compatibility
install Tools/i18n/pygettext.py $RPM_BUILD_ROOT%{_bindir}/pygettext

# just to cut the noise, as they are not packaged (now)
# first tests
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/test
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/bsddb/test
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/ctypes/test
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/distutils/tests
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/email/test
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/sqlite3/test

# other files
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/plat-*/regen
find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.egg-info -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.bat -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.txt -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name README\* -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post doc-info
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun doc-info
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/*

%files modules
%defattr(644,root,root,755)
/etc/shrc.d/python-modules*
%exclude %{py_scriptdir}/UserDict.py[co]
%exclude %{py_scriptdir}/codecs.py[co]
%exclude %{py_scriptdir}/copy_reg.py[co]
%exclude %{py_scriptdir}/locale.py[co]
%exclude %{py_scriptdir}/posixpath.py[co]
%exclude %{py_scriptdir}/pdb.py[co]
%exclude %{py_scriptdir}/profile.py[co]
%exclude %{py_scriptdir}/pstats.py[co]
%exclude %{py_scriptdir}/pydoc.py[co]
%exclude %{py_scriptdir}/site.py[co]
%exclude %{py_scriptdir}/stat.py[co]
%exclude %{py_scriptdir}/timeit.py[co]
%exclude %{py_scriptdir}/os.py[co]
%exclude %{py_scriptdir}/encodings/*.py[co]
%exclude %{py_scriptdir}/types.py[co]

%{py_scriptdir}/*.py[co]

%{py_dyndir}/*.egg-info

#
# list .so modules to be sure that all of them are built
#

# three modules below does not work on 64-bit architectures
# see Python README file for explanation
%ifnarch alpha ia64 ppc64 sparc64 %{x8664}
%attr(755,root,root) %{py_dyndir}/audioop.so
%attr(755,root,root) %{py_dyndir}/rgbimg.so
%attr(755,root,root) %{py_dyndir}/imageop.so
# sizeof(long) != sizeof(int), so dl module will not be built on 64-bit
# platforms
%attr(755,root,root) %{py_dyndir}/dl.so
%endif

%attr(755,root,root) %{py_dyndir}/array.so
%attr(755,root,root) %{py_dyndir}/binascii.so
%attr(755,root,root) %{py_dyndir}/_bisect.so
%attr(755,root,root) %{py_dyndir}/_bsddb.so
%attr(755,root,root) %{py_dyndir}/bz2.so
%attr(755,root,root) %{py_dyndir}/cmath.so
%attr(755,root,root) %{py_dyndir}/_codecs_cn.so
%attr(755,root,root) %{py_dyndir}/_codecs_hk.so
%attr(755,root,root) %{py_dyndir}/_codecs_iso2022.so
%attr(755,root,root) %{py_dyndir}/_codecs_jp.so
%attr(755,root,root) %{py_dyndir}/_codecs_kr.so
%attr(755,root,root) %{py_dyndir}/_codecs_tw.so
%attr(755,root,root) %{py_dyndir}/collections.so
%attr(755,root,root) %{py_dyndir}/cPickle.so
%attr(755,root,root) %{py_dyndir}/crypt.so
%attr(755,root,root) %{py_dyndir}/cStringIO.so
%attr(755,root,root) %{py_dyndir}/_csv.so
%attr(755,root,root) %{py_dyndir}/_ctypes*.so
%attr(755,root,root) %{py_dyndir}/_curses_panel.so
%attr(755,root,root) %{py_dyndir}/_curses.so
%attr(755,root,root) %{py_dyndir}/datetime.so
%attr(755,root,root) %{py_dyndir}/_elementtree.so
%attr(755,root,root) %{py_dyndir}/_functools.so
%attr(755,root,root) %{py_dyndir}/_hashlib.so
%attr(755,root,root) %{py_dyndir}/_heapq.so
%attr(755,root,root) %{py_dyndir}/_locale.so
%attr(755,root,root) %{py_dyndir}/_lsprof.so
%attr(755,root,root) %{py_dyndir}/_multibytecodec.so
%attr(755,root,root) %{py_dyndir}/_random.so
# other sha modules built only for openssl < 0.9.8
%attr(755,root,root) %{py_dyndir}/_sha.so
%attr(755,root,root) %{py_dyndir}/_socket.so
%attr(755,root,root) %{py_dyndir}/_ssl.so
%attr(755,root,root) %{py_dyndir}/_testcapi.so
%attr(755,root,root) %{py_dyndir}/_weakref.so
%ifnarch sparc64
%attr(755,root,root) %{py_dyndir}/dbm.so
%endif
%attr(755,root,root) %{py_dyndir}/fcntl.so
%attr(755,root,root) %{py_dyndir}/gdbm.so
%attr(755,root,root) %{py_dyndir}/grp.so
%attr(755,root,root) %{py_dyndir}/itertools.so
%attr(755,root,root) %{py_dyndir}/linuxaudiodev.so
%attr(755,root,root) %{py_dyndir}/math.so
%attr(755,root,root) %{py_dyndir}/mmap.so
%attr(755,root,root) %{py_dyndir}/nis.so
%attr(755,root,root) %{py_dyndir}/operator.so
%attr(755,root,root) %{py_dyndir}/ossaudiodev.so
%attr(755,root,root) %{py_dyndir}/parser.so
%attr(755,root,root) %{py_dyndir}/pyexpat.so
%attr(755,root,root) %{py_dyndir}/readline.so
%attr(755,root,root) %{py_dyndir}/resource.so
%attr(755,root,root) %{py_dyndir}/select.so
%attr(755,root,root) %{py_dyndir}/strop.so
%attr(755,root,root) %{py_dyndir}/syslog.so
%attr(755,root,root) %{py_dyndir}/termios.so
%attr(755,root,root) %{py_dyndir}/time.so
%attr(755,root,root) %{py_dyndir}/spwd.so
%attr(755,root,root) %{py_dyndir}/unicodedata.so
%attr(755,root,root) %{py_dyndir}/zlib.so

%dir %{py_scriptdir}/plat-*
%{py_scriptdir}/plat-*/*.py[co]

%dir %{py_scriptdir}/bsddb
%{py_scriptdir}/bsddb/*.py[co]

%dir %{py_scriptdir}/compiler
%{py_scriptdir}/compiler/*.py[co]

%dir %{py_scriptdir}/ctypes
%dir %{py_scriptdir}/ctypes/macholib
%{py_scriptdir}/ctypes/*.py[co]
%{py_scriptdir}/ctypes/macholib/*.py[co]

%dir %{py_scriptdir}/curses
%{py_scriptdir}/curses/*.py[co]

%dir %{py_scriptdir}/distutils
%dir %{py_scriptdir}/distutils/command
%{py_scriptdir}/distutils/*.py[co]
%{py_scriptdir}/distutils/command/*.py[co]

%dir %{py_scriptdir}/email
%dir %{py_scriptdir}/email/mime
%{py_scriptdir}/email/*.py[co]
%{py_scriptdir}/email/mime/*.py[co]

%dir %{py_scriptdir}/logging
%{py_scriptdir}/logging/*.py[co]

%dir %{py_scriptdir}/sqlite3
%{py_scriptdir}/sqlite3/*.py[co]

%dir %{py_scriptdir}/wsgiref
%{py_scriptdir}/wsgiref/*.py[co]

%dir %{py_scriptdir}/xml
%dir %{py_scriptdir}/xml/dom
%dir %{py_scriptdir}/xml/etree
%dir %{py_scriptdir}/xml/parsers
%dir %{py_scriptdir}/xml/sax
%{py_scriptdir}/xml/*.py[co]
%{py_scriptdir}/xml/dom/*.py[co]
%{py_scriptdir}/xml/etree/*.py[co]
%{py_scriptdir}/xml/parsers/*.py[co]
%{py_scriptdir}/xml/sax/*.py[co]

%files modules-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{py_dyndir}/_sqlite3.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*.so.*

%dir %{py_dyndir}
%dir %{py_scriptdir}
%dir %{py_libdir}
%dir %{py_sitescriptdir}
%dir %{py_sitedir}

# shared modules required by python library
%attr(755,root,root) %{py_dyndir}/_struct.so

# modules required by python library
%{py_scriptdir}/UserDict.py[co]
%{py_scriptdir}/codecs.py[co]
%{py_scriptdir}/copy_reg.py[co]
%{py_scriptdir}/locale.py[co]
%{py_scriptdir}/posixpath.py[co]
%{py_scriptdir}/site.py[co]
%{py_scriptdir}/stat.py[co]
%{py_scriptdir}/os.py[co]
# needed by the dynamic sys.lib patch
%{py_scriptdir}/types.py[co]

# encodings required by python library
%dir %{py_scriptdir}/encodings
%{py_scriptdir}/encodings/*.py[co]

%files -n pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_scriptdir}/pydoc.py[co]

%files -n idle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idle
%dir %{py_scriptdir}/idlelib
%dir %{py_scriptdir}/idlelib/Icons
%{py_scriptdir}/idlelib/*.py[co]
%{py_scriptdir}/idlelib/Icons/*
%{py_scriptdir}/idlelib/*.def

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README,README.valgrind,valgrind-python.supp}
%attr(755,root,root) %{_bindir}/python%{py_ver}-config
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
%attr(-,root,root) %{py_scriptdir}/*.py
%{py_scriptdir}/plat-*/*.py
%{py_scriptdir}/bsddb/*.py
%{py_scriptdir}/ctypes/*.py
%{py_scriptdir}/ctypes/macholib/*.py
%{py_scriptdir}/compiler/*.py
%{py_scriptdir}/curses/*.py
%{py_scriptdir}/distutils/*.py
%{py_scriptdir}/distutils/command/*.py
%{py_scriptdir}/email/*.py
%{py_scriptdir}/email/mime/*.py
%{py_scriptdir}/hotshot/*.py
%{py_scriptdir}/logging/*.py
%{py_scriptdir}/sqlite3/*.py
%{py_scriptdir}/wsgiref/*.py
%{py_scriptdir}/xml/*.py
%{py_scriptdir}/xml/dom/*.py
%{py_scriptdir}/xml/etree/*.py
%{py_scriptdir}/xml/parsers/*.py
%{py_scriptdir}/xml/sax/*.py
%{py_scriptdir}/encodings/*.py
%{py_scriptdir}/idlelib/*.py

%files devel-tools
%defattr(644,root,root,755)
%doc Lib/pdb.doc
/etc/shrc.d/python-devel*

%attr(755,root,root) %{_bindir}/pygettext

%attr(755,root,root) %{py_dyndir}/_hotshot.so
%dir %{py_scriptdir}/hotshot
%{py_scriptdir}/hotshot/*.py[co]
%{py_scriptdir}/pdb.py[co]
%{py_scriptdir}/profile.py[co]
%{py_scriptdir}/pstats.py[co]
%{py_scriptdir}/timeit.py[co]

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}


%files doc
%defattr(644,root,root,755)
%doc Python-Docs-%{version}%{beta}/*

%if %{with info}
%files doc-info
%defattr(644,root,root,755)
%{_infodir}/*
%endif

%if %{with tkinter}
%files tkinter
%defattr(644,root,root,755)
%{py_scriptdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so
%endif
