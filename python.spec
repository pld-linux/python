#
# TODO
# - test_pydoc fails because of PYTHONPATH override
# - change searchpath order so /usr/lib* is before /usr/share
# - kill lib-tk from searchpath
# - kill BR: file requirement from lib64 patch
# - security(CVE-2008-4108)
#   http://securitytracker.com/alerts/2008/Sep/1020904.html
#
# Conditional build:
%bcond_with	info			# build info pages (requires emacs, fails in python-2.5.0)
%bcond_without	tkinter			# disables tkinter module building
%bcond_without	tests			# disables Python testing
%bcond_with	verbose_tests		# runs tests in verbose mode
%bcond_with	openssl097		# build for openssl < 0.9.8
#
# tests which will not work on 64-bit platforms
%define		no64bit_tests	test_audioop test_rgbimg test_imageop
# tests which may fail because of builder environment limitations (no /proc or /dev/pts)
%define		nobuilder_tests test_resource test_openpty test_socket test_nis test_posix test_locale test_pty test_urllib2
# tests which fail because of some unknown/unresolved reason (this list should be ideally just %{nil})
%define		broken_tests test_doctest test_pydoc test_distutils test_gdb

%define	beta		%{nil}

%define py_ver		2.7
%define py_prefix	%{_prefix}
%define py_libdir	%{py_prefix}/%{_lib}/python%{py_ver}
%define py_incdir	%{_includedir}/python%{py_ver}
%define py_sitedir	%{py_libdir}/site-packages
%define py_sitescriptdir %{_datadir}/python%{py_ver}/site-packages
%define py_dyndir	%{py_libdir}/lib-dynload

%define dver %{version}
Summary:	Very high level scripting language with X interface
Summary(es.UTF-8):	Lenguaje script de alto nivel con interfaz X
Summary(fr.UTF-8):	Langage de script de très haut niveau avec interface X
Summary(pl.UTF-8):	Python - język obiektowy wysokiego poziomu
Summary(pt_BR.UTF-8):	Linguagem de programação interpretada de alto nível
Summary(ru.UTF-8):	Язык программирования очень высокого уровня с X-интерфейсом
Summary(tr.UTF-8):	X arayüzlü, yüksek düzeyli, kabuk yorumlayıcı dili
Summary(uk.UTF-8):	Мова програмування дуже високого рівня з X-інтерфейсом
Name:		python
Version:	%{py_ver}.14
Release:	1
Epoch:		1
License:	PSF
Group:		Development/Languages/Python
Source0:	https://www.python.org/ftp/python/%{version}/Python-%{version}%{beta}.tar.xz
# Source0-md5:	1f6db41ad91d9eb0a6f0c769b8613c5b
Source1:	https://www.python.org/ftp/python/doc/%{dver}/%{name}-%{dver}-docs-html.tar.bz2
# Source1-md5:	ab5f82c3198370f4ad91638f653629da
Source2:	pyconfig.h.in
Patch0:		%{name}-db.patch
Patch1:		%{name}-pythonpath.patch
Patch2:		%{name}-ac_fixes.patch
Patch3:		%{name}-multilib.patch
Patch4:		%{name}-verbose.patch
Patch5:		%{name}-distro.patch
Patch6:		%{name}-DNStests.patch
Patch7:		%{name}-install_prefix.patch
Patch8:		%{name}-bdist_rpm.patch
# https://bugs.python.org/issue10496
Patch9:		https://bugs.python.org/file21896/nonexistent_user.patch
# Patch9-md5:	db706fbe6de467c6e4c97c675eddf29a
URL:		https://www.python.org/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	bzip2-devel
BuildRequires:	db-devel >= 4
%{?with_info:BuildRequires:	emacs >= 21}
BuildRequires:	expat-devel >= 1:1.95.7
BuildRequires:	file
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	gmp-devel >= 4.0
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-ext-devel >= 5.2
BuildRequires:	pkgconfig
%if %{with openssl097}
BuildRequires:	openssl-devel < 0.9.8
%else
BuildRequires:	openssl-devel >= 0.9.8
%endif
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.3.5
%{?with_info:BuildRequires:	tetex-makeindex}
#%{?with_tkinter:BuildRequires:	tix-devel >= 1:8.1.4-4}
%{?with_tkinter:BuildRequires:	tk-devel >= 8.4.3}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Suggests:	python-pip
Obsoletes:	python2
Conflicts:	bzr < 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with verbose_tests}
%define test_flags -v -l -x
%else
%define test_flags -w -l -x
%endif

%ifarch alpha ia64 ppc64 ppc64 %{x8664}
%define test_list %{nobuilder_tests} %{broken_tests} %{no64bit_tests}
%else
%define test_list %{nobuilder_tests} %{broken_tests}
%endif

%ifarch sparc sparcv9
%define test_list %{nobuilder_tests} %{broken_tests} test_fcntl test_ioctl
%endif

%ifarch sparc64
%define test_list %{nobuilder_tests} %{broken_tests} %{no64bit_tests} test_fcntl test_ioctl
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

%description -l de.UTF-8
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

%description -l es.UTF-8
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga dinámica de objetos, clases, módulos y
excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca a
través de código C, tornando Python fácil de usar en ambientes
particulares/personalizados. Este paquete Python incluye la mayoría de
los módulos padrón Python, junto con módulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

%description -l fr.UTF-8
Python est un langage de script interprété et orienté objet. Il gère
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles bibliothèques systèmes
avec du code C est simple, ce qui rend Python facile à utiliser dans
des configs personnalisées.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfaçage avec les widgets Tix pour Tk
et RPM.

%description -l pl.UTF-8
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
językiem programowania. Jest modularny, obsługuje wyjątki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python łączy w
sobie duże możliwości i przejrzystą składnię. Posiada interfejsy do
wielu wywołań systemowych i bibliotek, w tym również do różnych
bibliotek okienkowych. Możliwości jego można jeszcze rozszerzać
poprzez odpowiednie moduły pisane w C lub C++. Python może być również
użyty jako element aplikacji, którym potrzebny jest interpreter do
skryptów. I wreszcie, Python jest wieloplatformowy, działa na wielu
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

Ten pakiet zawiera binarkę Pythona.

%description -l pt_BR.UTF-8
Python é uma linguagem de scripts interpretada orientada a objetos.
Contém suporte para carga dinâmica de objetos, classes, módulos e
exceções. Adicionar interfaces para novos sistemas de biblioteca
através de código C é simples, tornando Python fácil de usar em
ambientes particulares/personalizados.

Este pacote Python inclui a maioria do módulos padrão Python, junto
com módulos para interfaceamento para o conjunto de componentes Tix
para Tk e RPM.

%description -l ru.UTF-8
Python - это интерпретируемый, объектно-ориентированный язык
программирования. Он поддерживает динамическую загрузку объектов,
классы, модули и обработку исключительных ситуаций (exceptions).
Простота добавления интерфейсов к новым системным библиотекам через
код на языке C делает Python хорошим выбором для использования в
специальных конфигурациях.

%description -l tr.UTF-8
Python, nesneye yönelik bir kabuk yorumlayıcıdır. Nesnelerin,
sınıfların, modüllerin ve aykırı durumların dinamik yüklenmelerine
destek verir. C koduyla birlikte kullanımı son derece kolaydır. Bu
paket, standart Python birimlerinin çoğunun yanısıra Tk ve RPM için
arayüz birimlerini de içerir.

%description -l uk.UTF-8
Python - це інтерпретована, об'єктно-орієнтована мова програмування.
Він підтримує динамічну загрузку об'єктів, класи, модулі та обробку
виключних ситуацій (exceptions). Простота додавання інтерфейсів для
нових системних бібліотек через код на мові C робить Python добрим
вибором для використання в спеціальних конфігураціях.

%package libs
Summary:	Python library
Summary(pl.UTF-8):	Biblioteka języka Python
Group:		Libraries/Python
# broken detection in rpm/pythondeps.sh
Provides:	python(abi) = %{py_ver}
# for compatibility with existing Ac packages
Provides:	python(bytecode) = %{py_ver}
%{!?with_info:Obsoletes:	python-doc-info}
Obsoletes:	python-intl

%description libs
Python shared library and very essental modules for Python binary.

%description libs -l pl.UTF-8
Biblioteka współdzielona języka Python oraz bardzo podstawowe moduły
dla Pythona.

%package modules
Summary:	Python modules
Summary(pl.UTF-8):	Moduły języka Python
Group:		Libraries/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	python-argparse = 1.1
Provides:	python-cElementTree
Provides:	python-elementtree
Provides:	pythonegg(argparse) = 1.1
Obsoletes:	python-argparse < 1.1.99
Obsoletes:	python-cElementTree
Obsoletes:	python-ctypes
Obsoletes:	python-curses
Obsoletes:	python-elementtree
Obsoletes:	python-gdbm
Obsoletes:	python-hashlib
Obsoletes:	python-logging
Obsoletes:	python-old
Obsoletes:	python-optik
Obsoletes:	python-ssl
Obsoletes:	python-xml
Obsoletes:	python-xmlrpc <= 1.0.1
Obsoletes:	python-zlib
%requires_ge_to	openssl	openssl-devel

%description modules
Python officially distributed modules.

%description modules -l pl.UTF-8
Oficjalnie rozprowadzane moduły języka Python.

%package modules-sqlite
Summary:	Python SQLite modules
Summary(pl.UTF-8):	Moduły SQLite języka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Provides:	python(sqlite)

%description modules-sqlite
Python officially distributed sqlite module.

%description modules-sqlite -l pl.UTF-8
Oficjalnie rozprowadzany moduł sqlite języka Python.

%package -n pydoc
Summary:	Python interactive module documentation access support
Summary(pl.UTF-8):	Interaktywne korzystanie z dokumentacji modułów języka Python
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	python-pydoc

%description -n pydoc
Python interactive module documentation access support.

%description -n pydoc -l pl.UTF-8
Interaktywne korzystanie z dokumentacji modułów języka Python.

%package -n idle
Summary:	IDE for Python language
Summary(pl.UTF-8):	IDE dla języka Python
Group:		Applications/Editors
Requires:	%{name}-tkinter = %{epoch}:%{version}-%{release}
Obsoletes:	python-idle

%description -n idle
IDE for Python language.

%description -n idle -l pl.UTF-8
IDE dla języka Python.

%package devel
Summary:	Libraries and header files for building python code
Summary(de.UTF-8):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para construir programas en python
Summary(fr.UTF-8):	Bibliothèques et en-têtes pour construire du code python
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki Pythona
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para o Python
Summary(ru.UTF-8):	Библиотеки и хедеры для построения кода на языке Python
Summary(tr.UTF-8):	Python ile geliştirme yapmak için gerekli dosyalar
Summary(uk.UTF-8):	Бібліотеки та хедери для програмування на мові Python
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	python2-devel

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This package
contains the header files and libraries which are needed to do both of
these tasks.

%description devel -l de.UTF-8
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und läßt sich in andere Programme
integrieren. Dieses Paket enthält die Header-Dateien und Libraries,
die für beide Aufgaben erforderlich sind.

%description devel -l es.UTF-8
El interpretador Python permite incluir con facilidad extensiones
cargadas dinámicamente. Python es también fácil de ser empotrado en
otros programas. Este paquete contiene los archivos de inclusión y
bibliotecas necesarios para estas dos tareas.

%description devel -l fr.UTF-8
L'interpréteur Python est relativement facile à étendre avec des
extensions chargées dynamiquement et à insérer dans d'autres
programmes. Ce paquetage contient les en-têtes et les bibliothèques
nécessaires à ces deux tâches.

%description devel -l pl.UTF-8
Interpreter Pythona jest w miarę łatwy do rozszerzania przy pomocy
dynamicznie ładowanych rozszerzeń napisanych w C lub C++ oraz
osadzania w innych programach. Ten pakiet zawiera pliki nagłówkowe i
wszystko inne co potrzebne do tych celów.

%description devel -l pt_BR.UTF-8
O interpretador Python permite incluir com facilidade extensões
carregadas dinamicamente. Python é também fácil de ser embutido em
outros programas. Este pacote contém os arquivos de inclusão e
bibliotecas necessários para estas duas tarefas.

%description devel -l ru.UTF-8
Интерпретатор Python относительно легко расширяется при помощи
динамически загружаемых расширений и встраивается в другие программы.
Этот пакет содержит хедеры и библиотеки, необходимые для обеих этих
задач.

%description devel -l tr.UTF-8
Bu paket, Python ile geliştirme yapılabilmesi için gerekli başlık
dosyalarını ve kitaplıkları içerir.

%description devel -l uk.UTF-8
Інтерпретатор Python відносно легко розширюється за допомогою
розширень з динамічною загрузкою та вбудовується в інші програми. Цей
пакет містить хедери та бібліотеки, необхідні для обох цих задач.

%package devel-src
Summary:	Python module sources
Summary(pl.UTF-8):	Pliki źródłowe modułów Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-src
Python module sources.

%description devel-src -l pl.UTF-8
Pliki źródłowe modułów Pythona.

%package devel-tools
Summary:	Python development tools
Summary(pl.UTF-8):	Narzędzia programistyczne języka Python
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-tools
Python development tools such as profilers and debugger.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne języka Python takie jak profiler oraz
debugger.

%package 2to3
Summary:	Automated Python 2 to 3 code translation
Summary(pl.UTF-8):	Automatyczne tłumaczenie kodu Pythona 2 na 3
Group:		Development/Languages/Python

%description 2to3
2to3 is a Python program that reads Python 2.x source code and applies
a series of fixers to transform it into valid Python 3.x code. The
standard library contains a rich set of fixers that will handle almost
all code. 2to3 supporting library lib2to3 is, however, a flexible and
generic library, so it is possible to write your own fixers for 2to3.
lib2to3 could also be adapted to custom applications in which Python
code needs to be edited automatically.

%description 2to3 -l pl.UTF-8
2to3 to program w Pythonie czytający od źródłowy w Pythonie 2.x i
aplikujący serię poprawek przekształcających go w poprawny kod w
Pythonie 3.x. Biblioteka standardowa zawiera duży zbiór poprawek
obsługujących większość kodu. Biblioteka wspierająca 2to3 (lib2to3)
jest jednak elastyczną i ogólną biblioteką, więc można pisać własne
poprawki dla 2to3. lib2to3 można także zaadaptować na potrzeby
własnych zastosowań, w których kod w Pythonie musi być modyfikowany
automatycznie.

%package static
Summary:	Static python library
Summary(pl.UTF-8):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static python library.

%description static -l pl.UTF-8
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de.UTF-8):	Dokumentation zu Python
Summary(es.UTF-8):	Documentación para Python
Summary(fr.UTF-8):	Documentation sur Python
Summary(pl.UTF-8):	Dokumentacja do Pythona
Summary(pt_BR.UTF-8):	Documentação para a linguagem de programação Python
Summary(ru.UTF-8):	Документация по языку Python
Summary(tr.UTF-8):	Python belgeleri
Summary(uk.UTF-8):	Документація по мові Python
Group:		Documentation
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description doc -l de.UTF-8
Dieses Paket enthält Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description doc -l es.UTF-8
Documentación para Python. Contiene archivos en texto y PostScript.

%description doc -l fr.UTF-8
Ce paquetage contient la documentation sur le langage python et sur
son interpréteur sous forme de fichiers ASCII et LaTeX.

%description doc -l pl.UTF-8
Oficjalna dokumentacja do Pythona. Zawiera przykładowe programy,
narzędzia i dokumentację. Strony podręcznika man znajdują się w
głównym pakiecie. Ten pakiet nie zawiera źródeł dokumentacji
napisanych w LaTeXu, tylko gotowe do wykorzystania pliki postscriptowe
i HTML.

%description doc -l pt_BR.UTF-8
O pacote python-doc contém documentação para a linguagem de
programação e para o interpretador Python. Fornecida em arquivos texto
e Postcript.

%description doc -l ru.UTF-8
Этот пакет содержит документацию по собственно языку Python и по
исполняющему его интерпретатору в виде набора текстовых файлов и
исходных текстов в формате LaTeX.

%description doc -l tr.UTF-8
Bu paket, Python dili ile ilgili belgeleri ve düz ASCII dosyaları ve
LaTeX kaynaklarının bir karışımı olan yorumlayıcıyı içerir.

%description doc -l uk.UTF-8
Цей пакет містить документацію по власне мові Python та по виконуючому
її інтерпретатору у вигляді набора текстових файлів та вихідних
текстів у форматі LaTeX.

%package doc-info
Summary:	Documentation on Python in texinfo format
Summary(pl.UTF-8):	Dokumentacja do Pythona w formacie texinfo
Group:		Documentation

%description doc-info
Documentation on Python in texinfo format.

%description doc-info -l pl.UTF-8
Dokumentacja do Pythona w formacie texinfo.

%package tkinter
Summary:	Standard Python interface to the Tk GUI toolkit
Summary(de.UTF-8):	Grafische Tk-Schnittstelle für Python
Summary(es.UTF-8):	Interfaz de GUI Tk para Python
Summary(fr.UTF-8):	Interface graphique Tk pour Python
Summary(pl.UTF-8):	Standardowy interfejs Pythona do biblioteki Tk
Summary(pt_BR.UTF-8):	Interface GUI Tk para Phyton
Summary(tr.UTF-8):	Python için grafik kullanıcı arayüzü
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	tcl >= 8.4.3
Requires:	tix >= 1:8.1.4-4
Requires:	tk >= 8.4.3
Obsoletes:	tkinter

%description tkinter
Standard Python interface to the Tk GUI toolkit.

%description tkinter -l de.UTF-8
Eine grafische Schnittstelle für Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description tkinter -l es.UTF-8
Una interfaz gráfica para Python, basada en Tcl/Tk, y usada por muchas
herramientas de configuración.

%description tkinter -l fr.UTF-8
Interface graphique pour Python, basée sur Tcl/Tk et utilisée par
beaucoup des outils de configuration.

%description tkinter -l pl.UTF-8
Standardowy interfejs Pythona do biblioteki Tk.

%description tkinter -l pt_BR.UTF-8
Uma interface gráfica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configuração.

%description tkinter -l ru.UTF-8
Графический интерфейс (GUI) для Python, построенный на Tcl/Tk.

%description tkinter -l tr.UTF-8
Python için Tcl/Tk'ye dayalı ve pek çok ayarlama aracı tarafından
kullanılan grafik bir arayüzdür.

%description tkinter -l uk.UTF-8
Графічний інтерфейс (GUI) для Python, побудований на Tcl/Tk.

%package examples
Summary:	Example programs in Python
Summary(pl.UTF-8):	Przykładowe programy w Pythonie
Group:		Development/Languages/Python
Obsoletes:	python-tools

%description examples
Example programs in Python.

These are for Python 2.3.4, not %{version}.

%description examples -l pl.UTF-8
Przykładowe programy w Pythonie.

Przykłady te są dla Pythona 2.3.4, nie %{version}.

%package test
Summary:	Python test modules
Summary(pl.UTF-8):	Moduły testowe Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Suggests:	%{name}-devel-src = %{epoch}:%{version}-%{release}

%description test
Python test modules.

Unit tests for Python, some may be reused for testing other Python
software.

%description test -l pl.UTF-8
Moduły testowe Pythona.

Niektóre z nich mogą być używane do testowania oprogramowania
napisanego w Pythonie.

%prep
%setup -q -n Python-%{version}%{beta}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

tar xjf %{SOURCE1}

sed -i -e 's#db_setup_debug = False#db_setup_debug = True#g' setup.py

# remove if Lib/plat-linux3 exists
[ -d Lib/plat-linux3 ] && exit 1
cp -a Lib/plat-linux2 Lib/plat-linux3

%build
%{__aclocal}
%{__autoconf}
%configure \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	ac_cv_posix_semaphores_enabled=yes \
	ac_cv_broken_sem_getvalue=no \
	%{?with_debug:--with-pydebug} \
	--with-threads \
	--with-system-ffi \
	--enable-ipv6 \
	--enable-unicode=ucs4 \
	--enable-shared \
	--with-dbmliborder=gdbm:bdb \
	--without-ensurepip

%{__make} 2>&1 | awk '
BEGIN { fail = 0; logmsg = ""; }
{
		if ($0 ~ /\*\*\* WARNING:/) {
				fail = 1;
				logmsg = logmsg $0;
		}
		print $0;
}
END { if (fail) { print "\nPROBLEMS FOUND:"; print logmsg; exit(1); } }'

LC_ALL=C
export LC_ALL
%if %{with tests}
WITHIN_PYTHON_RPM_BUILD=1 %{__make} -j1 test \
	TESTOPTS="%{test_flags} %{test_list}" \
	TESTPYTHON="LD_LIBRARY_PATH=`pwd` PYTHONHOME=`pwd` PYTHONPATH=`pwd`/Lib:`pwd`/Lib/lib-tk:`pwd`/build/lib.linux-`uname -m`-%{py_ver} ./python -tt"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{py_sitescriptdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_infodir} \
	$RPM_BUILD_ROOT%{_docdir} \
	$RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# docs in constant location
ln -sf python-doc-%{version} $RPM_BUILD_ROOT%{_docdir}/python-doc

%if %{with info}
%{__make} -C Doc/info
cp -p Doc/info/python*info* $RPM_BUILD_ROOT%{_infodir}
%endif

cp -p Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

mv $RPM_BUILD_ROOT{%{py_libdir}/config,%{_libdir}}/libpython%{py_ver}.a
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython%{py_ver}.so

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

#
# create several useful aliases, such as timeit.py, profile.py, pdb.py, smtpd.py
#

# for python devel tools
for script in timeit profile pdb pstats; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-devel.csh

# for python modules
for script in smtpd webbrowser; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh
%{__rm} $RPM_BUILD_ROOT%{_bindir}/smtpd.py

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-modules.csh

# just to cut the noise, as they are not packaged (now)
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/ctypes/macholib/fetch_macholib
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/distutils/command/command_template
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/distutils/command/wininst-*.exe
%{__rm} -r $RPM_BUILD_ROOT%{py_libdir}/idlelib/idle_test
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/idlelib/ChangeLog
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/idlelib/help.html
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/idlelib/idle.pyw
%{__rm} -r $RPM_BUILD_ROOT%{py_libdir}/plat-*/regen
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{py_libdir}/pdb.doc

find $RPM_BUILD_ROOT%{py_libdir} -name \*.bat -exec rm {} \;
find $RPM_BUILD_ROOT%{py_libdir} -name \*.txt -exec rm {} \;
find $RPM_BUILD_ROOT%{py_libdir} -name README\* -exec rm {} \;

%{__mv} $RPM_BUILD_ROOT%{py_incdir}/pyconfig.h $RPM_BUILD_ROOT%{py_libdir}/config/pyconfig.h
sed -e's#@PREFIX@#%{_prefix}#g;s#@PY_VER@#%{py_ver}#g' %{SOURCE2} > $RPM_BUILD_ROOT%{py_incdir}/pyconfig.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig

%postun	libs -p /sbin/ldconfig

%post	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%attr(755,root,root) %{_bindir}/python2
%attr(755,root,root) %{_bindir}/python%{py_ver}
%{_mandir}/man1/python.1*
%{_mandir}/man1/python2.1*

%files modules
%defattr(644,root,root,755)
%doc Lib/pdb.doc
/etc/shrc.d/python-modules*
%exclude %{py_libdir}/_abcoll.py[co]
%exclude %{py_libdir}/abc.py[co]
%exclude %{py_libdir}/UserDict.py[co]
%exclude %{py_libdir}/codecs.py[co]
%exclude %{py_libdir}/copy_reg.py[co]
%exclude %{py_libdir}/genericpath.py[co]
%exclude %{py_libdir}/linecache.py[co]
%exclude %{py_libdir}/locale.py[co]
%exclude %{py_libdir}/posixpath.py[co]
%exclude %{py_libdir}/profile.py[co]
%exclude %{py_libdir}/pstats.py[co]
%exclude %{py_libdir}/pydoc.py[co]
%exclude %{py_libdir}/re.py[co]
%exclude %{py_libdir}/site.py[co]
%exclude %{py_libdir}/sre_*.py[co]
%exclude %{py_libdir}/stat.py[co]
%exclude %{py_libdir}/sysconfig.py[co]
%exclude %{py_libdir}/timeit.py[co]
%exclude %{py_libdir}/os.py[co]
%exclude %{py_libdir}/_weakrefset.py[co]
%exclude %{py_libdir}/encodings/*.py[co]
%exclude %{py_libdir}/types.py[co]
%exclude %{py_libdir}/warnings.py[co]

%{py_libdir}/*.py[co]

%{py_dyndir}/Python-%{version}-py%{py_ver}.egg-info

#
# list .so modules to be sure that all of them are built
#

# three modules below do not work on 64-bit architectures
# see Python README file for explanation
%ifnarch alpha ia64 ppc64 sparc64 %{x8664}
%attr(755,root,root) %{py_dyndir}/imageop.so
# sizeof(long) != sizeof(int), so dl module will not be built on 64-bit
# platforms
%attr(755,root,root) %{py_dyndir}/dl.so
%endif

%attr(755,root,root) %{py_dyndir}/audioop.so
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
%attr(755,root,root) %{py_dyndir}/_collections.so
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
%attr(755,root,root) %{py_dyndir}/_io.so
%attr(755,root,root) %{py_dyndir}/_json.so
%attr(755,root,root) %{py_dyndir}/_locale.so
%attr(755,root,root) %{py_dyndir}/_lsprof.so
%attr(755,root,root) %{py_dyndir}/_multibytecodec.so
%attr(755,root,root) %{py_dyndir}/_multiprocessing.so
%attr(755,root,root) %{py_dyndir}/_random.so
%{?with_openssl097:%attr(755,root,root) %{py_dyndir}/_sha*.so}
%attr(755,root,root) %{py_dyndir}/_socket.so
%attr(755,root,root) %{py_dyndir}/_ssl.so
%attr(755,root,root) %{py_dyndir}/_testcapi.so
%ifnarch sparc64
%attr(755,root,root) %{py_dyndir}/dbm.so
%endif
%attr(755,root,root) %{py_dyndir}/fcntl.so
%attr(755,root,root) %{py_dyndir}/future_builtins.so
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

%dir %{py_libdir}/plat-*
%{py_libdir}/plat-*/*.py[co]

%dir %{py_libdir}/bsddb
%{py_libdir}/bsddb/*.py[co]

%dir %{py_libdir}/compiler
%{py_libdir}/compiler/*.py[co]

%dir %{py_libdir}/ctypes
%dir %{py_libdir}/ctypes/macholib
%{py_libdir}/ctypes/*.py[co]
%{py_libdir}/ctypes/macholib/*.py[co]

%dir %{py_libdir}/curses
%{py_libdir}/curses/*.py[co]

%dir %{py_libdir}/distutils
%dir %{py_libdir}/distutils/command
%{py_libdir}/distutils/*.py[co]
%{py_libdir}/distutils/command/*.py[co]

%dir %{py_libdir}/email
%dir %{py_libdir}/email/mime
%{py_libdir}/email/*.py[co]
%{py_libdir}/email/mime/*.py[co]

%dir %{py_libdir}/ensurepip
%{py_libdir}/ensurepip/*.py[co]
%{py_libdir}/ensurepip/_bundled

%dir %{py_libdir}/idlelib

%dir %{py_libdir}/importlib
%{py_libdir}/importlib/*.py[co]

%dir %{py_libdir}/json
%{py_libdir}/json/*.py[co]

%dir %{py_libdir}/logging
%{py_libdir}/logging/*.py[co]

%dir %{py_libdir}/multiprocessing
%dir %{py_libdir}/multiprocessing/dummy
%{py_libdir}/multiprocessing/*.py[co]
%{py_libdir}/multiprocessing/dummy/*.py[co]

%dir %{py_libdir}/unittest
%{py_libdir}/unittest/*.py[co]
%dir %{py_libdir}/unittest/test
%{py_libdir}/unittest/test/*.py[co]

%dir %{py_libdir}/wsgiref
%{py_libdir}/wsgiref/*.py[co]
%{py_libdir}/wsgiref.egg-info

%dir %{py_libdir}/xml
%dir %{py_libdir}/xml/dom
%dir %{py_libdir}/xml/etree
%dir %{py_libdir}/xml/parsers
%dir %{py_libdir}/xml/sax
%{py_libdir}/xml/*.py[co]
%{py_libdir}/xml/dom/*.py[co]
%{py_libdir}/xml/etree/*.py[co]
%{py_libdir}/xml/parsers/*.py[co]
%{py_libdir}/xml/sax/*.py[co]

%files modules-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{py_dyndir}/_sqlite3.so
%dir %{py_libdir}/sqlite3
%{py_libdir}/sqlite3/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython%{py_ver}.so.*

%dir %{py_dyndir}
%dir %{py_libdir}
%dir %{_datadir}/python%{py_ver}
%dir %{py_sitescriptdir}
%dir %{py_sitedir}

# shared modules required by python library
%attr(755,root,root) %{py_dyndir}/_struct.so

# modules required by python library
%{py_libdir}/_abcoll.py[co]
%{py_libdir}/abc.py[co]
%{py_libdir}/UserDict.py[co]
%{py_libdir}/codecs.py[co]
%{py_libdir}/copy_reg.py[co]
%{py_libdir}/genericpath.py[co]
%{py_libdir}/linecache.py[co]
%{py_libdir}/locale.py[co]
%{py_libdir}/posixpath.py[co]
%{py_libdir}/re.py[co]
%{py_libdir}/site.py[co]
%{py_libdir}/sre_*.py[co]
%{py_libdir}/stat.py[co]
%{py_libdir}/sysconfig.py[co]
%{py_libdir}/os.py[co]
%{py_libdir}/_weakrefset.py[co]
# needed by the dynamic sys.lib patch
%{py_libdir}/types.py[co]
%{py_libdir}/warnings.py[co]

# encodings required by python library
%dir %{py_libdir}/encodings
%{py_libdir}/encodings/*.py[co]

# required by sysconfig.py
%dir %{py_libdir}/config
%{py_libdir}/config/Makefile
%{py_libdir}/config/pyconfig.h
%dir %{py_incdir}
%{py_incdir}/pyconfig.h

%files -n pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_libdir}/pydoc.py[co]
%dir %{py_libdir}/pydoc_data
%{py_libdir}/pydoc_data/*.py[co]

%files -n idle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idle
%dir %{py_libdir}/idlelib/Icons
%{py_libdir}/idlelib/*.py[co]
%{py_libdir}/idlelib/Icons/*
%{py_libdir}/idlelib/*.def

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README,README.valgrind,valgrind-python.supp}
%attr(755,root,root) %{_bindir}/python-config
%attr(755,root,root) %{_bindir}/python2-config
%attr(755,root,root) %{_bindir}/python%{py_ver}-config
%attr(755,root,root) %{_libdir}/libpython%{py_ver}.so
%attr(755,root,root) %{_libdir}/libpython.so
%{py_incdir}/*.h
%exclude %{py_incdir}/pyconfig.h
%{_pkgconfigdir}/python.pc
%{_pkgconfigdir}/python2.pc
%{_pkgconfigdir}/python-%{py_ver}.pc

%attr(755,root,root) %{py_libdir}/config/makesetup
%attr(755,root,root) %{py_libdir}/config/install-sh
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
%{py_libdir}/bsddb/*.py
%{py_libdir}/ctypes/*.py
%{py_libdir}/ctypes/macholib/*.py
%{py_libdir}/compiler/*.py
%{py_libdir}/curses/*.py
%{py_libdir}/distutils/*.py
%{py_libdir}/distutils/command/*.py
%{py_libdir}/email/*.py
%{py_libdir}/email/mime/*.py
%{py_libdir}/encodings/*.py
%{py_libdir}/hotshot/*.py
%{py_libdir}/ensurepip/*.py
%{py_libdir}/idlelib/*.py
%{py_libdir}/importlib/*.py
%{py_libdir}/json/*.py
%{py_libdir}/lib2to3/*.py
%{py_libdir}/lib2to3/fixes/*.py
%{py_libdir}/lib2to3/pgen2/*.py
%{py_libdir}/logging/*.py
%{py_libdir}/multiprocessing/*.py
%{py_libdir}/multiprocessing/dummy/*.py
%{py_libdir}/pydoc_data/*.py
%{py_libdir}/sqlite3/*.py
%{py_libdir}/unittest/*.py
%{py_libdir}/unittest/test/*.py
%{py_libdir}/wsgiref/*.py
%{py_libdir}/xml/*.py
%{py_libdir}/xml/dom/*.py
%{py_libdir}/xml/etree/*.py
%{py_libdir}/xml/parsers/*.py
%{py_libdir}/xml/sax/*.py

%files devel-tools
%defattr(644,root,root,755)
/etc/shrc.d/python-devel*

%attr(755,root,root) %{py_dyndir}/_hotshot.so
%dir %{py_libdir}/hotshot
%{py_libdir}/hotshot/*.py[co]
%{py_libdir}/profile.py[co]
%{py_libdir}/pstats.py[co]
%{py_libdir}/timeit.py[co]

%files 2to3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/2to3
%dir %{py_libdir}/lib2to3
%dir %{py_libdir}/lib2to3/fixes
%dir %{py_libdir}/lib2to3/pgen2
%{py_libdir}/lib2to3/*.py[co]
%{py_libdir}/lib2to3/*.pickle
%{py_libdir}/lib2to3/fixes/*.py[co]
%{py_libdir}/lib2to3/pgen2/*.py[co]

%files static
%defattr(644,root,root,755)
%{_libdir}/libpython%{py_ver}.a
%{_libdir}/libpython.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files test
%defattr(644,root,root,755)
%{py_libdir}/test
%{py_libdir}/bsddb/test
%{py_libdir}/ctypes/test
%{py_libdir}/distutils/tests
%{py_libdir}/email/test
%{py_libdir}/sqlite3/test
%{py_libdir}/json/tests
%{py_libdir}/lib2to3/tests

%files doc
%defattr(644,root,root,755)
%doc python-%{dver}-docs-html/*
%{_docdir}/python-doc

%if %{with info}
%files doc-info
%defattr(644,root,root,755)
%{_infodir}/*.info*
%endif

%if %{with tkinter}
%files tkinter
%defattr(644,root,root,755)
%{py_libdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so
%endif
