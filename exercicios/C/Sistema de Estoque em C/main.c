#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gtk/gtk.h>

#define MAX_ITEMS 100
#define MAX_NAME_LENGTH 50

typedef struct {
    char name[MAX_NAME_LENGTH];
    int quantity;
} Item;

Item stock[MAX_ITEMS];
int itemCount = 0;

GtkWidget *nameEntry;
GtkWidget *quantityEntry;
GtkWidget *listTextView;

void addItem(GtkWidget *widget, gpointer data) {
    const char *name = gtk_entry_get_text(GTK_ENTRY(nameEntry));
    const char *quantityStr = gtk_entry_get_text(GTK_ENTRY(quantityEntry));
    int quantity = atoi(quantityStr);

    if (itemCount >= MAX_ITEMS) {
        gtk_label_set_text(GTK_LABEL(listTextView), "Estoque cheio. Impossível adicionar mais itens.");
        return;
    }

    strcpy(stock[itemCount].name, name);
    stock[itemCount].quantity = quantity;

    itemCount++;
    gtk_label_set_text(GTK_LABEL(listTextView), "Item adicionado ao estoque com sucesso.");
}

void listItems(GtkWidget *widget, gpointer data) {
    char buffer[1000] = "Estoque:\n";

    for (int i = 0; i < itemCount; i++) {
        char itemEntry[100];
        snprintf(itemEntry, sizeof(itemEntry), "%s - Quantidade: %d\n", stock[i].name, stock[i].quantity);
        strcat(buffer, itemEntry);
    }

    gtk_label_set_text(GTK_LABEL(listTextView), buffer);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Sistema de Estoque");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 200);
    gtk_container_set_border_width(GTK_CONTAINER(window), 10);

    GtkWidget *grid = gtk_grid_new();
    gtk_grid_set_row_spacing(GTK_GRID(grid), 5);
    gtk_grid_set_column_spacing(GTK_GRID(grid), 5);
    gtk_container_add(GTK_CONTAINER(window), grid);

    GtkWidget *nameLabel = gtk_label_new("Nome do item:");
    gtk_grid_attach(GTK_GRID(grid), nameLabel, 0, 0, 1, 1);

    nameEntry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), nameEntry, 1, 0, 1, 1);

    GtkWidget *quantityLabel = gtk_label_new("Quantidade:");
    gtk_grid_attach(GTK_GRID(grid), quantityLabel, 0, 1, 1, 1);

    quantityEntry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), quantityEntry, 1, 1, 1, 1);

    GtkWidget *addItemButton = gtk_button_new_with_label("Adicionar Item");
    g_signal_connect(addItemButton, "clicked", G_CALLBACK(addItem), NULL);
    gtk_grid_attach(GTK_GRID(grid), addItemButton, 0, 2, 2, 1);

    GtkWidget *listButton = gtk_button_new_with_label("Listar Itens");
    g_signal_connect(listButton, "clicked", G_CALLBACK(listItems), NULL);
    gtk_grid_attach(GTK_GRID(grid), listButton, 0, 3, 2, 1);

    listTextView = gtk_label_new("Estoque:");
    gtk_grid_attach(GTK_GRID(grid), listTextView, 0, 4, 2, 1);

    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
