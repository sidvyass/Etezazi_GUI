import tkinter as tk
import specs


def selection_boxes(root, create_drop_down_menu, event_select, add_element):
    """Builds all the elements of the program on the screen - connects to main page, except root, all passed values
    are functions"""
    # This could be changed to put into a loop but this gives me more control over where I want all the elements
    # All the Boxes for inputs and their labels
    tk.Label(root, text="Select OEM").grid(row=1, column=0, padx=5, pady=5)
    oem_box = create_drop_down_menu(root, specs.oem, 30, 2, 0)
    oem_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.oem, 0))

    tk.Label(root, text="Select Material").grid(row=3, column=0, padx=5, pady=5)
    material_box = create_drop_down_menu(root, specs.material, 30, 4, 0)
    material_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.material, 1))

    tk.Label(root, text="Select NDT").grid(row=5, column=0, padx=5, pady=5)
    ndt_box = create_drop_down_menu(root, specs.ndt, width=30, row=6, column=0)
    ndt_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.ndt, 2, add_one=False))

    tk.Label(root, text="Select Anodize").grid(row=7, column=0, padx=5, pady=5)
    anodize_box = create_drop_down_menu(root, specs.anodize, width=30, row=8, column=0)
    anodize_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.anodize, 3, add_one=False))

    tk.Label(root, text="Select Chem-film").grid(row=1, column=1, padx=5, pady=5)
    chem_film_box = create_drop_down_menu(root, specs.chem_film, width=30, row=2, column=1)
    chem_film_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.chem_film, 4, add_one=False))

    tk.Label(root, text="Select Masking (omit primer)").grid(row=3, column=1, padx=5, pady=5)
    masking_box = create_drop_down_menu(root, specs.masking_omit_primer, width=30, row=4, column=1)
    masking_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.masking_omit_primer, 5, add_one=False))

    tk.Label(root, text="Select PRIME").grid(row=5, column=1, padx=5, pady=5)
    prime_box = create_drop_down_menu(root, specs.prime, width=30, row=6, column=1)
    prime_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.prime, 6, add_one=False))

    tk.Label(root, text="Select Masking (Omit Top Coat)").grid(row=7, column=1, padx=5, pady=5)
    mask_box = create_drop_down_menu(root, specs.masking_omit_top_coat, width=30, row=8, column=1)
    mask_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.masking_omit_top_coat, 7, add_one=False))

    tk.Label(root, text="Select Top Coat").grid(row=1, column=2, padx=5, pady=5)
    top_coat_box = create_drop_down_menu(root, specs.top_coat, width=30, row=2, column=2)
    top_coat_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.top_coat, 8, add_one=False))

    tk.Label(root, text="MISC 1").grid(row=3, column=2, padx=5, pady=5)
    misc_box = create_drop_down_menu(root, specs.misc_1, width=30, row=4, column=2)
    misc_box.bind("<<ComboboxSelected>>", lambda event: event_select(event, specs.misc_1, 9, add_one=False))

    # BUTTONS FOR ADDING

    oem_button = tk.Button(root, text="Add OEM", command=lambda: add_element(specs.oem, oem_box))
    oem_button.grid(row=10, column=2, padx=5, pady=5)

    material_button = tk.Button(root, text="Add Material", command=lambda: add_element(specs.material, material_box))
    material_button.grid(row=11, column=2, padx=5, pady=5)

    ndt_button = tk.Button(root, text="Add NDT", command=lambda: add_element(specs.ndt, ndt_box))
    ndt_button.grid(row=12, column=2, padx=5, pady=5)

    anodize_button = tk.Button(root, text="Add Anodize", command=lambda: add_element(specs.anodize, anodize_box))
    anodize_button.grid(row=13, column=2, padx=5, pady=5)

    chem_film_button = tk.Button(root, text="Add ChemFilm", command=lambda: add_element(specs.anodize, anodize_box))
    chem_film_button.grid(row=14, column=2, padx=5, pady=5)

    masking_primer = tk.Button(root, text="Add Masking Primer",
                               command=lambda: add_element(specs.masking_omit_primer, masking_box))
    masking_primer.grid(row=15, column=2, padx=5, pady=5)

    prime_button = tk.Button(root, text="Add Prime", command=lambda: add_element(specs.prime, prime_box))
    prime_button.grid(row=16, column=2, padx=5, pady=5)

    masking_button = tk.Button(root, text="Add Masking (omit top coat)",
                               command=lambda: add_element(specs.masking_omit_top_coat, mask_box))
    masking_button.grid(row=17, column=2, padx=5, pady=5)

    top_coat_button = tk.Button(root, text="Add Top Coat", command=lambda: add_element(specs.top_coat, top_coat_box))
    top_coat_button.grid(row=18, column=2, padx=5, pady=5)

    misc1_button = tk.Button(root, text="Add Misc1", command=lambda: add_element(specs.misc_1, misc_box))
    misc1_button.grid(row=19, column=2, padx=5, pady=5)