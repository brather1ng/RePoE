# RePoE

Repository of Path of Exile resources for tool developers.

Contains only information about stat and mod id resolution at the moment. See the `data`
folder for those files and the `docs` folder for their documentation.

For the actual GGPK parsing, [PyPoE](https://github.com/OmegaK2/PyPoE) is used.
The code here just converts PyPoE's Python objects to JSON.

Developed to supply [PoESkillTree](https://github.com/EmmittJ/PoESkillTree) with the
game data information it requires. I'll only convert files that are necessary for
PoESkillTree. But I'm open to requests about converted files or Pull Requests that
add conversion for more files.

## Files

The `data` folder contains the generated data in Json format. Each file has a
formatted and a compact version. The formatted versions complement their descriptions
in the `docs` folder.

Note that the file formats are not yet final, they may change at any time. Once
they are more stable, I'll probably make releases every time the game has updates
that changes these files.
