
#
# todo:
# - fix locale test to use configured locale instead of en_US (or sth.)
#

# Conditional build:
%bcond_without tkinter	# disables tkinter module building
%bcond_without tests	# disables Python testing
#
%define py_ver         2.3
%define py_prefix      %{_prefix}
%define py_libdir      %{py_prefix}/%{_lib}/python%{py_ver}
%define py_scriptdir   %{py_prefix}/share/python%{py_ver}
%define py_incdir      %{_includedir}/python%{py_ver}
%define py_sitedir     %{py_libdir}/site-packages
%define py_sitescriptdir %{py_scriptdir}/site-packages
%define py_dyndir      %{py_libdir}/lib-dynload
%define py_comp        ./python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"
%define py_ocomp       ./python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"

Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-OberflДche
Summary(es):	Lenguaje script de alto nivel con interface X
Summary(fr):	Langage de script de tИs haut niveau avec interface X
Summary(pl):	Python - jЙzyk obiektowy wysokiego poziomu
Summary(pt_BR):	Linguagem de programaГЦo interpretada, orientada a objeto de alto nМvel
Summary(ru):	Язык программирования очень высокого уровня с X-интерфейсом
Summary(tr):	X arayЭzlЭ, yЭksek dЭzeyli, kabuk yorumlayЩcЩ dili
Summary(uk):	Мова програмування дуже високого р╕вня з X-╕нтерфейсом
Name:		python
Version:	%{py_ver}.3
Release:	1.2
Epoch:		1
License:	PSF
Group:		Applications
Source0:	http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
# Source0-md5:	70ada9f65742ab2c77a96bcd6dffd9b1
Source1:	http://www.python.org/ftp/python/doc/%{version}/html-%{version}.tar.bz2
# Source1-md5:	5ec6e5782a3caf5177a3d47272a0267f
Patch0:		%{name}-readline.patch
Patch1:		%{name}-%{name}path.patch
Patch2:		%{name}-default_encoding.patch
Patch3:		%{name}-no_ndbm.patch
Patch4:		%{name}-ac_fixes.patch
Patch5:		%{name}-noarch_to_datadir.patch
Patch6:		%{name}-lib64.patch
Patch7:		%{name}-doc_path.patch
URL:		http://www.python.org/
BuildRequires:	autoconf
BuildRequires:	db-devel >= 4
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	gmp-devel => 4.0
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	readline-devel >= 4.2
%{?with_tkinter:BuildRequires:	tix-devel >= 1:8.1.4-4}
%{?with_tkinter:BuildRequires:	tk-devel >= 8.4.3}
BuildRequires:	zlib-devel
Requires:	python-libs = %{epoch}:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	%{name} = %{py_ver}
Obsoletes:	python-xml
Obsoletes:	python-intl
Obsoletes:	python-curses
Obsoletes:	python-gdbm
Obsoletes:	python-zlib
Obsoletes:	python2
Obsoletes:	python2-devel

# tests which will not work on 64-bit platforms
%define		no64bit_tests	test_audioop test_rgbimg test_imageop
# tests which may fail because of builder environment limitations (no /proc or /dev/pts)
%define		nobuilder_tests test_resource test_openpty test_socket
# test which fail because of some unknown/unresolved reason (this list should be empty)
%define		broken_tests	test_anydbm test_bsddb test_re test_shelve test_whichdb test_zipimport

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
articulares/ personalizados. Este paquete Python incluye la mayorМa de
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
Provides:	%{name}-libs = %{py_ver}

%description libs
Python library.

%description libs -l pl
Biblioteka jЙzyka Python.

%package modules
Summary:	Python modules
Summary(pl):	ModuЁy jЙzyka Python
Group:		Libraries/Python
Provides:	%{name}-modules = %{py_ver}
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	python-logging
Obsoletes:	python-xmlrpc <= 1.0.1

%description modules
Python modules.

%description modules -l pl
ModuЁy jЙzyka Python.

%package -n pydoc
Summary:	Python interactive module documentation access support
Summary(pl):	Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}
Obsoletes:	python-pydoc

%description -n pydoc
Python interactive module documentation access support.

%description -n pydoc -l pl
Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python.

%package -n idle
Summary:	IDE for Python language
Summary(pl):	IDE dla jЙzyka Python
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}
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
Requires:	%{name}-libs = %{epoch}:%{version}

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
Requires:	%{name}-modules = %{epoch}:%{version}

%description devel-src
Python module sources.

%description devel-src -l pl
Pliki ╪rСdЁowe moduЁСw Pythona.

%package devel-tools
Summary:	Python development tools
Summary(pl):	NarzЙdzia programistyczne jЙzyka Python
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}
Requires:	%{name} = %{epoch}:%{version}

%description devel-tools
Python development tools such as profilers and debugger.

%description devel-tools -l pl
NarzЙdzia programistyczne jЙzyka Python takie jak profiler oraz debugger.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Provides:	%{name}-static = %{py_ver}
Requires:	%{name}-devel = %{epoch}:%{version}

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
Requires:	%{name} = %{epoch}:%{version}
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
napisanych w LaTeXu, tylko gotowe do wykorzystania pliki
postscriptowe i HTML.

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

%package tkinter
Summary:	Standard Python interface to the Tk GUI toolkit
Summary(de):	Grafischer OberflДche fЭr Python
Summary(es):	Interface GUI para Phyton
Summary(fr):	Interface graphique pour python
Summary(pl):	Standardowy interfejs Pythona do biblioteki Tk
Summary(pt_BR):	Interface GUI para Phyton
Summary(tr):	Python iГin grafik kullanЩcЩ arayЭzЭ
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}
Requires:	tcl >= 8.0.3
Requires:	tk  >= 8.0.3
Requires:	tix >= 4.1.0.6
Obsoletes:	tkinter

%description tkinter
Standard Python interface to the Tk GUI toolkit.

%description tkinter -l de
Eine grafische Schnittstelle fЭr Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description tkinter -l es
Una interface grАfica para Python, basada en Tcl/Tk, y usada por
muchas herramientas de configuraciСn.

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

%package old
Summary:	Depreciated Python modules
Summary(pl):	Nieaktualne moduЁy jЙzyka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}

%description old
Install this package when one of your program written in Python is old
as Miss Universum of 1918, who only you want to see... ooops, which
only you want to run.

%description old -l pl
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich programСw napisanych
w jЙzyku Python jest tak stary jak Miss Universum z roku 1918, ktСr╠
tylko ty chcesz zobaczyФ... przepraszam, ktСry tylko ty chcesz
uruchomiФ.

%package examples
Summary:	Example programs in Python
Summary(pl):	PrzykЁadowe programy w Pythonie
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}
Obsoletes:	python-tools

%description examples
Example programs in Python.

%description examples -l pl
PrzykЁadowe programy w Pythonie.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%ifarch amd64
%patch6 -p1
%endif
%patch7 -p1

tar -xf %{SOURCE1} --use=bzip2

%build
%{__autoconf}

CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure \
	--with-threads \
	--enable-unicode=ucs4 \
	--enable-shared

%{__make} \
	OPT="%{rpmcflags}"

LC_ALL=C
export LC_ALL
%if %{with tests}
%ifarch alpha sparc64 ppc64 amd64
%{__make} test TESTOPTS="-l -x %{no64bit_tests} %{nobuilder_tests} %{broken_tests}"
%else
%{__make} test TESTOPTS="-l -x %{nobuilder_tests} %{broken_tests}"
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{py_sitescriptdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

install libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython%{py_ver}.so

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# create several useful scripts, such as timeit.py, profile.py, pdb.py
for script in timeit.py profile.py pdb.py pstats.py; do
    cat <<END > $RPM_BUILD_ROOT%{_bindir}/$script
#!/bin/sh
exec python %{py_libdir}/${script}c "\$@"
END
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/*

# readline support for python binary
%attr(755,root,root) %{py_dyndir}/readline.so

%files modules
%defattr(644,root,root,755)
%exclude %{py_libdir}/UserDict.py[co]
%exclude %{py_libdir}/codecs.py[co]
%exclude %{py_libdir}/copy_reg.py[co]
%exclude %{py_libdir}/locale.py[co]
%exclude %{py_libdir}/posixpath.py[co]
%exclude %{py_libdir}/pdb.py[co]
%exclude %{py_libdir}/profile.py[co]
%exclude %{py_libdir}/pstats.py[co]
%exclude %{py_libdir}/pydoc.py[co]
%exclude %{py_libdir}/site.py[co]
%exclude %{py_libdir}/stat.py[co]
%exclude %{py_libdir}/timeit.py[co]
%exclude %{py_libdir}/os.py[co]
%exclude %{py_libdir}/encodings/*.py[co]

%{py_libdir}/*.py[co]

#
# list .so modules to be sure that all of them are built
#

# three modules below does not work on 64-bit architectures
# see Python README file for explanation
%ifnarch alpha sparc64 ppc64 amd64
%attr(755,root,root) %{py_dyndir}/audioop.so
%attr(755,root,root) %{py_dyndir}/rgbimg.so
%attr(755,root,root) %{py_dyndir}/imageop.so
# sizeof(long) != sizeof(int), so dl module will not be built on 64-bit
# platforms
%attr(755,root,root) %{py_dyndir}/dl.so
%endif

%attr(755,root,root) %{py_dyndir}/_bsddb.so
%attr(755,root,root) %{py_dyndir}/_csv.so
%attr(755,root,root) %{py_dyndir}/_curses.so
%attr(755,root,root) %{py_dyndir}/_curses_panel.so
%attr(755,root,root) %{py_dyndir}/_locale.so
%attr(755,root,root) %{py_dyndir}/_random.so
%attr(755,root,root) %{py_dyndir}/_socket.so
%attr(755,root,root) %{py_dyndir}/_ssl.so
%attr(755,root,root) %{py_dyndir}/_testcapi.so
%attr(755,root,root) %{py_dyndir}/_weakref.so
%attr(755,root,root) %{py_dyndir}/array.so
%attr(755,root,root) %{py_dyndir}/binascii.so
%attr(755,root,root) %{py_dyndir}/bz2.so
%attr(755,root,root) %{py_dyndir}/cPickle.so
%attr(755,root,root) %{py_dyndir}/cStringIO.so
%attr(755,root,root) %{py_dyndir}/cmath.so
%attr(755,root,root) %{py_dyndir}/crypt.so
%attr(755,root,root) %{py_dyndir}/datetime.so
%attr(755,root,root) %{py_dyndir}/dbm.so
%attr(755,root,root) %{py_dyndir}/fcntl.so
%attr(755,root,root) %{py_dyndir}/gdbm.so
%attr(755,root,root) %{py_dyndir}/grp.so
%attr(755,root,root) %{py_dyndir}/itertools.so
%attr(755,root,root) %{py_dyndir}/linuxaudiodev.so
%attr(755,root,root) %{py_dyndir}/math.so
%attr(755,root,root) %{py_dyndir}/md5.so
%attr(755,root,root) %{py_dyndir}/mmap.so
%attr(755,root,root) %{py_dyndir}/mpz.so
%attr(755,root,root) %{py_dyndir}/nis.so
%attr(755,root,root) %{py_dyndir}/operator.so
%attr(755,root,root) %{py_dyndir}/ossaudiodev.so
%attr(755,root,root) %{py_dyndir}/parser.so
%attr(755,root,root) %{py_dyndir}/pcre.so
%attr(755,root,root) %{py_dyndir}/pwd.so
%attr(755,root,root) %{py_dyndir}/pyexpat.so
%attr(755,root,root) %{py_dyndir}/regex.so
%attr(755,root,root) %{py_dyndir}/resource.so
%attr(755,root,root) %{py_dyndir}/rotor.so
%attr(755,root,root) %{py_dyndir}/select.so
%attr(755,root,root) %{py_dyndir}/sha.so
%attr(755,root,root) %{py_dyndir}/strop.so
%attr(755,root,root) %{py_dyndir}/syslog.so
%attr(755,root,root) %{py_dyndir}/termios.so
%attr(755,root,root) %{py_dyndir}/time.so
%attr(755,root,root) %{py_dyndir}/timing.so
%attr(755,root,root) %{py_dyndir}/unicodedata.so
%attr(755,root,root) %{py_dyndir}/xreadlines.so
%attr(755,root,root) %{py_dyndir}/zlib.so

%dir %{py_libdir}/plat-*
%attr(755,root,root) %{py_libdir}/plat-*/regen
%{py_libdir}/plat-*/*.py[co]

%dir %{py_libdir}/bsddb
%{py_libdir}/bsddb/*.py[co]

%dir %{py_libdir}/compiler
%{py_libdir}/compiler/*.py[co]

%dir %{py_libdir}/curses
%{py_libdir}/curses/*.py[co]

%dir %{py_libdir}/distutils
%{py_libdir}/distutils/*.py[co]

%dir %{py_libdir}/distutils/command
%{py_libdir}/distutils/command/*.py[co]

%dir %{py_libdir}/email
%{py_libdir}/email/*.py[co]

%dir %{py_libdir}/logging
%{py_libdir}/logging/*.py[co]

%dir %{py_libdir}/xml
%{py_libdir}/xml/*.py[co]

%dir %{py_libdir}/xml/parsers
%{py_libdir}/xml/parsers/*.py[co]

%dir %{py_libdir}/xml/sax
%{py_libdir}/xml/sax/*.py[co]

%dir %{py_libdir}/xml/dom
%{py_libdir}/xml/dom/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*so.*

%dir %{py_dyndir}
%dir %{py_libdir}
%dir %{py_sitescriptdir}
%dir %{py_sitedir}

# required shared modules by python library
%attr(755,root,root) %{py_dyndir}/struct.so

# required modules by python library
%{py_libdir}/UserDict.py[co]
%{py_libdir}/codecs.py[co]
%{py_libdir}/copy_reg.py[co]
%{py_libdir}/locale.py[co]
%{py_libdir}/posixpath.py[co]
%{py_libdir}/site.py[co]
%{py_libdir}/stat.py[co]
%{py_libdir}/os.py[co]

# required encodings by python library
%dir %{py_libdir}/encodings
%{py_libdir}/encodings/*.py[co]

%files -n pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_libdir}/pydoc.py[co]

%files -n idle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idle
%dir %{py_libdir}/idlelib
%dir %{py_libdir}/idlelib/Icons
%{py_libdir}/idlelib/*.py[co]
%{py_libdir}/idlelib/Icons/*
%{py_libdir}/idlelib/*.def

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README}
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
%{py_libdir}/bsddb/*.py
%{py_libdir}/compiler/*.py
%{py_libdir}/curses/*.py
%{py_libdir}/distutils/*.py
%{py_libdir}/distutils/command/*.py
%{py_libdir}/email/*.py
%{py_libdir}/hotshot/*.py
%{py_libdir}/logging/*.py
%{py_libdir}/xml/*.py
%{py_libdir}/xml/parsers/*.py
%{py_libdir}/xml/sax/*.py
%{py_libdir}/xml/dom/*.py
%{py_libdir}/encodings/*.py
%{py_libdir}/idlelib/*.py

%files devel-tools
%defattr(644,root,root,755)
%doc Lib/profile.doc Lib/pdb.doc
%attr(755,root,root) %{_bindir}/timeit.py
%attr(755,root,root) %{_bindir}/profile.py
%attr(755,root,root) %{_bindir}/pdb.py
%attr(755,root,root) %{_bindir}/pstats.py

%attr(755,root,root) %{py_dyndir}/_hotshot.so
%dir %{py_libdir}/hotshot
%{py_libdir}/hotshot/*.py[co]
%{py_libdir}/pdb.py[co]
%{py_libdir}/profile.py[co]
%{py_libdir}/pstats.py[co]
%{py_libdir}/timeit.py[co]

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files doc
%defattr(644,root,root,755)
%doc Python-Docs-%{version}/*
%dir %{py_libdir}/test
%attr(-,root,root) %{py_libdir}/test/*
%attr(-,root,root) %{py_libdir}/email/test/*
%attr(-,root,root) %{py_libdir}/bsddb/test/*

%if %{with tkinter}
%files tkinter
%defattr(644,root,root,755)
%{py_libdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so
%endif

%files old
%defattr(644,root,root,755)
%dir %{py_libdir}/lib-old
%{py_libdir}/lib-old/*.py[co]
