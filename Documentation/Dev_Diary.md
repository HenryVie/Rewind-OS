# Rewind OS Development Diary

## 02/6/2026
- Installed Git
- Installed VS Code
- Created GitHub repository
- Attempted Virt-Manager installation but failed
- Repository mirror issue with rutabaga-gfx-ffi
- Decided to use VirtualBox for now
- Downloaded Fedora iso
- Created Fedora virtual machine, named it "Fedora Laboratory"

## 03/6/2026
- Cloned the GitHub repo to Fedora Lab
- Created and tested the first working Rewind OS script: /Scripts/install/install-packages.sh
- The script read package names from a text file and installs automatically using DNF
- Implemented profile-based package installation: /Scripts/install/install-profile.sh

    **Commands:**
  - ./install-profile.sh student
  - ./install-profile.sh gamer
  - ./install-profile.sh creator
  - ./install-profile.sh hobbyist
  - ./install-profile.sh beginner
    
  The script automatically installs:
  - Essential packages
  - Selected profile packages
Successfully tested with the Student profile.
