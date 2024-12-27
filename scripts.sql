-- Tabela de clientes
CREATE TABLE client (
    client_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Tabela de veículos
CREATE TABLE vehicle (
    vehicle_id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    license_plate TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

-- Tabela de reparações
CREATE TABLE work (
    work_id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    status TEXT CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled')) DEFAULT 'pending',
    cost REAL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id) ON DELETE CASCADE
);

-- Tabela de funcionários
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    role TEXT CHECK (role IN ('mechanic', 'manager', 'admin')) DEFAULT 'mechanic',
    hired_date DATE NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Tabela de tarefas
CREATE TABLE task (
    task_id INTEGER PRIMARY KEY,
    work_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    status TEXT CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled')) DEFAULT 'pending',
    start_date DATE NOT NULL,
    end_date DATE,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (work_id) REFERENCES work(work_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE SET NULL
);

-- Tabela de faturas
CREATE TABLE invoice (
    invoice_id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    total REAL NOT NULL,
    iva REAL NOT NULL,
    total_with_iva REAL NOT NULL,
    issued_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

-- Tabela para items da fatura
CREATE TABLE invoice_item (
    item_id INTEGER PRIMARY KEY,
    invoice_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,  -- Relacionamento com a task, não com o work
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES task(task_id) ON DELETE CASCADE
);


-- Tabela de configurações
CREATE TABLE setting (
    setting_id INTEGER PRIMARY KEY,
    key_name TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL,
    updated_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Inserir dados na tabela de clientes
INSERT INTO client (name, email, phone, address) VALUES
('João Silva', 'joao.silva@example.com', '912345678', 'Rua A, 123, Lisboa'),
('Maria Oliveira', 'maria.oliveira@example.com', '913456789', 'Av. B, 456, Porto'),
('Carlos Santos', 'carlos.santos@example.com', '914567890', 'Rua C, 789, Faro'),
('Ana Pereira', 'ana.pereira@example.com', '915678901', 'Rua D, 321, Coimbra'),
('Ricardo Gonçalves', 'ricardo.goncalves@example.com', '916789012', 'Av. E, 654, Braga');

-- Inserir dados na tabela de veículos
INSERT INTO vehicle (client_id, brand, model, year, license_plate) VALUES
(1, 'Toyota', 'Corolla', 2015, 'AA-12-BC'),
(1, 'Honda', 'Civic', 2018, 'BB-34-DE'),
(2, 'Ford', 'Focus', 2017, 'CC-56-FG'),
(3, 'BMW', '320i', 2020, 'DD-78-HI'),
(4, 'Volkswagen', 'Golf', 2016, 'EE-90-JK'),
(5, 'Renault', 'Clio', 2019, 'FF-12-LM'),
(5, 'Peugeot', '208', 2017, 'GG-34-NO'),
(3, 'Mercedes', 'A180', 2022, 'HH-56-PQ');

-- Inserir dados na tabela de reparações
INSERT INTO work (vehicle_id, description, status, cost, start_date, end_date) VALUES
(1, 'Troca de óleo e filtros', 'completed', 100.50, '2024-12-01', '2024-12-02'),
(2, 'Substituição de pastilhas de travão', 'in_progress', NULL, '2024-12-20', NULL),
(3, 'Revisão geral', 'pending', NULL, '2024-12-27', NULL),
(4, 'Reparação da suspensão', 'pending', NULL, '2024-12-28', NULL),
(5, 'Reparação do motor', 'completed', 450.00, '2024-11-15', '2024-11-18'),
(6, 'Pintura completa', 'completed', 800.00, '2024-12-05', '2024-12-10'),
(7, 'Substituição de bateria', 'completed', 120.00, '2024-12-15', '2024-12-16'),
(8, 'Troca de pneus', 'in_progress', NULL, '2024-12-22', NULL);

-- Inserir dados na tabela de funcionários
INSERT INTO employee (name, email, phone, role, hired_date) VALUES
('Rui Ferreira', 'rui.ferreira@example.com', '910123456', 'mechanic', '2023-01-15'),
('Ana Costa', 'ana.costa@example.com', '911234567', 'manager', '2022-06-10'),
('Pedro Martins', 'pedro.martins@example.com', '912345678', 'mechanic', '2024-02-20'),
('Tiago Almeida', 'tiago.almeida@example.com', '913456789', 'mechanic', '2024-03-10'),
('Sofia Lopes', 'sofia.lopes@example.com', '914567890', 'admin', '2021-11-01');

-- Inserir dados na tabela de tarefas
INSERT INTO task (work_id, employee_id, description, status, start_date, end_date) VALUES
(1, 1, 'Troca de óleo', 'completed', '2024-12-01', '2024-12-01'),
(1, 3, 'Troca de filtro de ar', 'completed', '2024-12-01', '2024-12-02'),
(2, 1, 'Substituir pastilhas dianteiras', 'in_progress', '2024-12-20', NULL),
(3, 3, 'Diagnóstico inicial', 'pending', '2024-12-27', NULL),
(5, 2, 'Inspeção final', 'completed', '2024-11-18', '2024-11-18'),
(6, 4, 'Aplicação de tinta', 'completed', '2024-12-05', '2024-12-08'),
(7, 1, 'Substituir bateria', 'completed', '2024-12-15', '2024-12-16'),
(8, 4, 'Troca dos pneus traseiros', 'in_progress', '2024-12-22', NULL);

-- Inserir dados na tabela de configurações
INSERT INTO setting (key_name, value) VALUES
('work_hours_per_day', '8'),
('default_task_status', 'pending'),
('notification_email', 'support@example.com'),
('max_tasks_per_employee', '5'),
('min_days_for_maintenance', '2');

-- Inserir dados na tabela de faturas (invoice)
INSERT INTO invoice (client_id, total, iva, total_with_iva) VALUES
(1, 100.50, 0.23, 100.50 * (1 + 0.23)),  -- Fatura do cliente 1 (João Silva) com o trabalho "Troca de óleo e filtros"
(5, 450.00, 0.23, 450.00 * (1 + 0.23)),  -- Fatura do cliente 5 (Ricardo Gonçalves) com o trabalho "Reparação do motor"
(6, 800.00, 0.23, 800.00 * (1 + 0.23)),  -- Fatura do cliente 6 (Renault) com o trabalho "Pintura completa"
(7, 120.00, 0.23, 120.00 * (1 + 0.23));  -- Fatura do cliente 7 (Substituição de bateria)

-- Inserir dados na tabela de itens de fatura (invoice_item)
INSERT INTO invoice_item (invoice_id, task_id, description, cost) VALUES
(1, 1, 'Troca de óleo', 50.00),  -- Tarefa 1 (Troca de óleo) do trabalho "Troca de óleo e filtros"
(1, 2, 'Troca de filtro de ar', 50.50),  -- Tarefa 2 (Troca de filtro de ar) do trabalho "Troca de óleo e filtros"
(5, 5, 'Inspeção final', 450.00),  -- Tarefa 5 (Inspeção final) do trabalho "Reparação do motor"
(6, 6, 'Aplicação de tinta', 800.00),  -- Tarefa 6 (Aplicação de tinta) do trabalho "Pintura completa"
(7, 7, 'Substituição de bateria', 120.00);  -- Tarefa 7 (Substituição de bateria) do trabalho "Substituição de bateria"

-- Inserir dados na tabela de configurações
INSERT INTO setting (key_name, value, updated_at) VALUES
('operating_hours', '09:00-18:00', '2024-12-23 07:31:03'),
('currency', 'EUR', '2024-12-23 07:31:03'),
('iva', '0,23', '2024-12-23 07:31:03'),
('labor_cost', '50', '2024-12-23 07:31:03');

