import os
import shutil
from pymol import cmd

def convert_cif_to_pdb(cif_path, pdb_path):
    base_name = os.path.splitext(os.path.basename(cif_path))[0]
    try:
        cmd.load(cif_path, base_name)
        cmd.save(pdb_path, base_name)
        cmd.delete("all")
        print(f"Converted: {base_name}.cif -> {base_name}.pdb")
    except Exception as e:
        print(f"Failed to convert {base_name}: {e}")

def main():
    cif_dir = "structures"
    backup_dir = os.path.join(cif_dir, "cif_backup")
    os.makedirs(backup_dir, exist_ok=True)

    for filename in os.listdir(cif_dir):
        if filename.endswith(".cif"):
            cif_path = os.path.join(cif_dir, filename)
            pdb_filename = filename.replace(".cif", ".pdb")
            pdb_path = os.path.join(cif_dir, pdb_filename)

            convert_cif_to_pdb(cif_path, pdb_path)

            # move original .cif to backup folder
            shutil.move(cif_path, os.path.join(backup_dir, filename))

if __name__ == "__main__":
    main()
