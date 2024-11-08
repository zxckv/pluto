# Pluto

Pluto is a Jupyter Notebook (.ipynb) to Python (.py) file converter.

## How It Works

The Jupyter Notebook is segmented into sections, each containing a block of markdown text. Each section will be appended to the top of a new file, under the assumption that each will be an individual question/problem.

> [!WARNING]
> Pluto is not perfect and does not remove any of the markdown segments. As such, it will sometimes create files that are of no use to you and they can be deleted.

## Usage

Download the latest release and use the application as follows:

```bash
./pluto my_notebook.ipynb
```

This will create a folder of the same name in the current working directory.

#### Multiple Files

The same can be acheived with multiple notebooks at the same time by just adding them sequestially as below:

```bash
./pluto my_notebook.ipynb other_notebook.ipynb
```
  
#### Name Overwrite

Pluto also supports the ability to overwrite the name of the created folder and files. This can be done using ```-o``` as seen in the example below: 

```bash
./pluto my_notebook.ipynb -o new_name
```

> [!NOTE] 
> You **cannot** use the name overwrite tag when dealing with multiple files. The first overwrite will work as expected, but any further overwrite tags will not and will instead use their original file name. To overwrite multiple files, please do them seperately.

#### Developer Mode

Using ```-d``` enables developer mode, providing verbose messages during the conversion process:

```bash
./pluto -d my_notebook.ipynb
```

> [!NOTE]
> Devloper mode will work in conjunction with any of the other options available. It can also be placed in any argument position.

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)