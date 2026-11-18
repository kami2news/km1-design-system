export interface ButtonProps { /** 外にある form の id（type="submit" のとき）/ id of a form outside the button */ form?: string; appearance?: 'primary'|'secondary'|'outline'|'subtle'|'transparent'; size?: 'small'|'medium'|'large'; disabled?: boolean; icon?: React.ReactNode; type?: 'button'|'submit'; onClick?: () => void; children?: React.ReactNode; 'aria-label'?: string; 'aria-describedby'?: string }
export interface InputProps { label?: string; required?: boolean; value?: string; defaultValue?: string; placeholder?: string; hint?: string; error?: string; disabled?: boolean; type?: string; id?: string; name?: string; autoComplete?: string; inputMode?: React.HTMLAttributes<HTMLInputElement>['inputMode']; span?: 'full'; onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void; onBlur?: (e: React.FocusEvent<HTMLInputElement>) => void }
export interface CheckboxProps { name?: string; checked?: boolean; defaultChecked?: boolean; disabled?: boolean; id?: string; onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void; children?: React.ReactNode }
export interface LinkProps { href: string; external?: boolean; onClick?: () => void; children?: React.ReactNode }
export interface AlertProps { status?: 'info'|'success'|'warning'|'danger'; title: string; label?: string; onClose?: () => void; children?: React.ReactNode }
export interface CardProps { /** 密度（既定 regular）。余白だけが変わり、操作領域は変わらない / Density (default regular): spacing only, never targets */ density?: 'compact' | 'regular' | 'spacious'; title?: string; headingLevel?: 2|3|4|5|6; onClick?: () => void; children?: React.ReactNode }
export interface BadgeProps { appearance?: 'brand'|'subtle'|'danger'|'success'|'warning'|'outline'; children?: React.ReactNode }
export interface SelectOption { value: string; label: string; disabled?: boolean }
export interface SelectProps { label?: string; required?: boolean; options: SelectOption[]; value?: string; defaultValue?: string; hint?: string; error?: string; disabled?: boolean; id?: string; name?: string; span?: 'full'; onChange?: (e: React.ChangeEvent<HTMLSelectElement>) => void; onBlur?: (e: React.FocusEvent<HTMLSelectElement>) => void }
export interface RadioGroupProps { id?: string; hint?: string; error?: string; span?: 'full'; legend: string; required?: boolean; options: SelectOption[]; value?: string; defaultValue?: string; name?: string; disabled?: boolean; onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void }
export interface SwitchProps { checked?: boolean; defaultChecked?: boolean; disabled?: boolean; id?: string; onLabel?: string; offLabel?: string; onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void; children?: React.ReactNode }
export interface TabItem { value: string; label: string; content: React.ReactNode }
export interface TabsProps { items: TabItem[]; label?: string; value?: string; defaultValue?: string; onChange?: (value: string) => void }
export interface DialogProps { open: boolean; title: string; onClose?: () => void; actions?: React.ReactNode; children?: React.ReactNode }

export interface TextareaProps { label: string; hint?: string; error?: string; required?: boolean; rows?: number; maxLength?: number; value?: string; defaultValue?: string; placeholder?: string; disabled?: boolean; id?: string; name?: string; span?: 'full'; onChange?: (e: any) => void; onBlur?: (e: React.FocusEvent<HTMLTextAreaElement>) => void; }
export declare function Textarea(props: TextareaProps): JSX.Element;
export interface ChipProps { selected?: boolean; onClick?: (e: any) => void; className?: string; children?: any; }
export declare function Chip(props: ChipProps): JSX.Element;
export interface ProgressProps { label: string; /** 省くと不確定 / omit for indeterminate */ value?: number; max?: number; valueText?: string; status?: 'success' | 'warning' | 'danger';
  /** 工程の名前 / step names */ steps?: string[]; /** 今の工程（0 始まり）/ current step, zero-based */ step?: number;
  /** 残り秒数。null で「計算中」/ seconds left; null = estimating */ remaining?: number | null; /** 経過秒数。残り時間を見積もれないときに使う / seconds elapsed, for work that cannot be estimated */ elapsed?: number; /** 見込みを超えた / past the estimate */ overdue?: boolean; onCancel?: () => void; className?: string; }
/** 残り秒数を「残り約 30 秒」の形にする / Formats seconds left */
export declare function formatRemaining(seconds: number | null): string | null;
export declare function Progress(props: ProgressProps): JSX.Element;
export interface SpinnerProps { label?: string; hideLabel?: boolean; className?: string; }
export declare function Spinner(props: SpinnerProps): JSX.Element;
export interface ToastProps { open: boolean; status?: 'info' | 'success' | 'warning' | 'danger'; action?: { label: string; onClick: () => void }; /** ミリ秒。省くと自動で消えない / ms; omit to stay */ duration?: number; onClose?: () => void; className?: string; children?: any; }
export declare function Toast(props: ToastProps): JSX.Element;
export interface MenuItem { label: string; onSelect?: () => void; icon?: any; danger?: boolean; disabled?: boolean; }
export interface MenuProps { label: string; items: MenuItem[]; icon?: any; iconOnly?: boolean; align?: 'start' | 'end'; appearance?: 'primary' | 'secondary' | 'subtle'; className?: string; }
export declare function Menu(props: MenuProps): JSX.Element;
export interface TableColumn { key: string; label: string; /** 行の読み上げ名に使う文字 / text for the row name */ text?: (row: any) => string; align?: 'start' | 'end'; sortable?: boolean; render?: (row: any) => any; }
export interface TableSort { key: string; direction: 'asc' | 'desc'; }
export interface TableBulkAction { label: string; onClick: (ids: any[]) => void; icon?: any; danger?: boolean; }
export interface TableProps { /** 密度（既定 regular）。余白だけが変わり、操作領域は変わらない / Density (default regular): spacing only, never targets */ density?: 'compact' | 'regular' | 'spacious'; selectable?: boolean; selected?: any[]; onSelectionChange?: (ids: any[]) => void; bulkActions?: TableBulkAction[]; caption: string; hideCaption?: boolean; columns: TableColumn[]; rows: any[]; sort?: TableSort; onSort?: (sort: TableSort) => void; rowHeader?: boolean; striped?: boolean; empty?: string; className?: string; }
export declare function Table(props: TableProps): JSX.Element;
export interface NavItem { value: string; label: string; icon: any; iconSelected?: any; href?: string; }
export interface NavProps { label: string; items: NavItem[]; value: string; onChange?: (value: string, e: any) => void; orientation?: 'auto' | 'horizontal' | 'vertical'; className?: string; }
export declare function Nav(props: NavProps): JSX.Element;
export interface CalendarProps { /** 'YYYY-MM-DD' */ value?: string; onChange?: (value: string) => void; /** {'2026-11-14': 件数} */ marks?: Record<string, number>; min?: string; max?: string; weekStart?: 0 | 1; label?: string; today?: string; className?: string; }
export declare function Calendar(props: CalendarProps): JSX.Element;
export interface TimetablePeriod { label: string; time?: string; }
export interface TimetableItem { day: number; period: number; title: string; sub?: string; /** cat-* の名前 / a cat-* name, e.g. 'teal' */ cat?: string; /** 分類の模様（しるしを題名の前に出す）/ category pattern; shows a mark before the title */ pattern?: CategoryPattern; }
export interface TimetableProps { caption: string; hideCaption?: boolean; days?: string[]; periods: TimetablePeriod[]; items: TimetableItem[]; today?: number; onSelect?: (item: TimetableItem) => void; className?: string; }
export declare function Timetable(props: TimetableProps): JSX.Element;
export interface TooltipProps { content: string; position?: 'top' | 'bottom'; align?: 'center' | 'start' | 'end'; delay?: number; className?: string; children: any; }
export declare function Tooltip(props: TooltipProps): JSX.Element;
export interface PaginationProps { page: number; count: number; onChange?: (page: number) => void; label?: string; className?: string; }
export declare function Pagination(props: PaginationProps): JSX.Element;
export interface EmptyStateProps { title: string; icon?: any; action?: any; headingLevel?: 2 | 3 | 4; className?: string; children?: any; }
export declare function EmptyState(props: EmptyStateProps): JSX.Element;
export interface SearchBoxProps { label: string; hideLabel?: boolean; placeholder?: string; value?: string; defaultValue?: string; onChange?: (value: string, e: any) => void; onSearch?: (value: string) => void; hint?: string; error?: string; id?: string; className?: string; }
export declare function SearchBox(props: SearchBoxProps): JSX.Element;
export interface ComboboxOption { value: string; label: string; disabled?: boolean; }
export interface ComboboxProps { label: string; options: ComboboxOption[]; value?: string; onChange?: (value: string, option: ComboboxOption) => void; placeholder?: string; hint?: string; error?: string; required?: boolean; disabled?: boolean; emptyText?: string; hideLabel?: boolean; id?: string; className?: string; }
export declare function Combobox(props: ComboboxProps): JSX.Element;
export interface SliderProps { label: string; min?: number; max?: number; step?: number; value?: number; defaultValue?: number; onChange?: (value: number, e: any) => void; unit?: string; valueText?: (value: number) => string; marks?: [string, string]; hint?: string; disabled?: boolean; id?: string; className?: string; }
export declare function Slider(props: SliderProps): JSX.Element;
export interface SpinButtonProps { label: string; value?: number; defaultValue?: number; onChange?: (value: number, e: any) => void; min?: number; max?: number; step?: number; unit?: string; hint?: string; error?: string; required?: boolean; disabled?: boolean; hideLabel?: boolean; id?: string; className?: string; }
export declare function SpinButton(props: SpinButtonProps): JSX.Element;
export interface AccordionItem { value: string; title: string; content: any; meta?: string; }
export interface AccordionProps { items: AccordionItem[]; multiple?: boolean; defaultOpen?: string[]; headingLevel?: 2 | 3 | 4 | 5 | 6; onChange?: (open: string[]) => void; className?: string; }
export declare function Accordion(props: AccordionProps): JSX.Element;
export interface DrawerProps { open: boolean; onClose?: () => void; title: string; actions?: any; position?: 'end' | 'start'; className?: string; children?: any; }
export declare function Drawer(props: DrawerProps): JSX.Element;
export interface BreadcrumbItem { label: string; href?: string; onClick?: (e: any) => void; }
export interface BreadcrumbProps { items: BreadcrumbItem[]; label?: string; className?: string; }
export declare function Breadcrumb(props: BreadcrumbProps): JSX.Element;
export interface SkeletonProps { shape?: 'text' | 'list' | 'card'; lines?: number; label?: string; className?: string; }
export declare function Skeleton(props: SkeletonProps): JSX.Element;
export interface FileUploadProps { label: string; onChange?: (files: File[]) => void; files?: Array<{ name: string; size?: number }>; accept?: string; multiple?: boolean; hint?: string; error?: string; required?: boolean; id?: string; className?: string; }
export declare function FileUpload(props: FileUploadProps): JSX.Element;
export interface AvatarProps { name: string; src?: string; initials?: string; size?: 'sm' | 'md' | 'lg'; color?: string; decorative?: boolean; className?: string; }
export declare function Avatar(props: AvatarProps): JSX.Element;
export interface TimeGridDay { /** 'YYYY-MM-DD' */ date: string; /** '11/12（木）' */ label: string; }
export interface TimeGridEvent { day: number; /** '9:00' */ start?: string; end?: string; title: string; sub?: string; /** cat-* の名前 */ cat?: string; /** 分類の模様 / category pattern */ pattern?: CategoryPattern; allDay?: boolean; kind?: 'event' | 'deadline'; tentative?: boolean; }
export interface TimeGridProps { label: string; days: TimeGridDay[]; events: TimeGridEvent[]; startHour?: number; endHour?: number; hourHeight?: number; height?: number; /** 'YYYY-MM-DDTHH:MM' */ now?: string; onSelect?: (event: TimeGridEvent) => void; className?: string; }
export declare function TimeGrid(props: TimeGridProps): JSX.Element;
export interface ToolbarItem { label?: string; icon?: any; onClick?: () => void; iconOnly?: boolean; pressed?: boolean; disabled?: boolean; priority?: 'normal' | 'low'; separator?: boolean; }
export interface ToolbarProps { label: string; items: ToolbarItem[]; className?: string; }
export declare function Toolbar(props: ToolbarProps): JSX.Element;
export interface PopoverProps { title: string; trigger: { label: string; icon?: any; iconOnly?: boolean; appearance?: 'primary' | 'secondary' | 'subtle' }; open?: boolean; onOpenChange?: (open: boolean) => void; align?: 'start' | 'end'; className?: string; children?: any; }
export declare function Popover(props: PopoverProps): JSX.Element;
export interface TagPickerProps { label: string; options: Array<{ value: string; label: string }>; value: string[]; onChange?: (value: string[]) => void; placeholder?: string; hint?: string; error?: string; required?: boolean; max?: number; id?: string; className?: string; }
export declare function TagPicker(props: TagPickerProps): JSX.Element;
export interface SortableItem { id: string; label: string; sub?: string; }
export interface SortableListProps { /** 密度（既定 regular）。余白だけが変わり、操作領域は変わらない / Density (default regular): spacing only, never targets */ density?: 'compact' | 'regular' | 'spacious'; label: string; items: SortableItem[]; onChange?: (items: SortableItem[]) => void; id?: string; className?: string; }
export declare function SortableList(props: SortableListProps): JSX.Element;

/* Forms (KM1-PAT-001) */
export interface FormGroupProps { title: string; description?: string; as?: 'section' | 'fieldset'; headingLevel?: 2 | 3 | 4; className?: string; children?: React.ReactNode }
export declare function FormGroup(props: FormGroupProps): JSX.Element;
export interface FormGridProps { columns?: 1 | 2; className?: string; children?: React.ReactNode }
export declare function FormGrid(props: FormGridProps): JSX.Element;
export declare function FormItem(props: { span?: 'full'; children?: React.ReactNode }): JSX.Element;
/** 子は PC の並び（左から: 戻る/キャンセル … 主ボタン）で渡す。幅 479px 以下では DOM 順ごと逆にし、主ボタンを上に置く。 */
export declare function FormActions(props: { className?: string; children?: React.ReactNode }): JSX.Element;
export interface ConditionalFieldProps { show: boolean; announce?: string; announceHide?: string; id?: string; className?: string; children?: React.ReactNode }
export declare function ConditionalField(props: ConditionalFieldProps): JSX.Element;
export interface FormError { id: string; label: string; message: string; name?: string }
export interface ErrorSummaryProps { errors: FormError[]; title?: string; focusKey?: number; /** 外から決める id（見出しは `${id}-title`）。省くと自動で振る / optional id; heading becomes `${id}-title` */ id?: string; className?: string }
export declare function ErrorSummary(props: ErrorSummaryProps): JSX.Element | null;
export interface UseFormConfig<V extends Record<string, any>> {
  initial?: Partial<V>;
  labels?: Partial<Record<keyof V, string>>;
  validate?: Partial<Record<keyof V, (value: any, all: V) => string | null | undefined>>;
  when?: Partial<Record<keyof V, (all: V) => boolean>>;
  resetOnHide?: (keyof V)[];
}
export interface UseForm<V extends Record<string, any>> {
  values: V; set: (name: keyof V, value: any) => void; visible: (name: keyof V) => boolean; submitCount: number;
  field: (name: keyof V, opts?: { kind?: 'text' | 'checkbox' | 'radio' | 'value' }) => Record<string, any>;
  errors: FormError[]; payload: () => Partial<V>;
  handleSubmit: (onValid: (data: Partial<V>) => void) => (e?: React.FormEvent) => void;
}
export declare function useForm<V extends Record<string, any>>(config?: UseFormConfig<V>): UseForm<V>;

/* 密度 / Density (KM1-TOK-001) */
export type Density = 'compact' | 'regular' | 'spacious';

/* KM1 × M1 (KM1-M1-001) */
export interface UseSelection<Id = string | number> { selected: Id[]; count: number; isSelected: (id: Id) => boolean; toggle: (id: Id) => void; set: (ids: Id[]) => void; clear: () => void; selectAll: (ids: Id[]) => void }
export declare function useSelection<Id = string | number>(initial?: Id[]): UseSelection<Id>;
export interface ContextualAction { label: string; onClick: () => void; icon?: React.ReactNode; danger?: boolean }
export interface ContextualActionBarProps { count: number; actions?: ContextualAction[]; onClear?: () => void; total?: number; onSelectAll?: () => void; label?: string; sticky?: boolean; className?: string }
export declare function ContextualActionBar(props: ContextualActionBarProps): JSX.Element;
export interface ListProps<Id = string | number> { label?: string; selectable?: boolean; selected?: Id[]; onSelectionChange?: (ids: Id[]) => void; dividers?: boolean; maxHeight?: number | string; className?: string; children?: React.ReactNode }
export declare function List(props: ListProps): JSX.Element;
export interface ListItemProps { id?: string | number; title: React.ReactNode; description?: React.ReactNode; meta?: React.ReactNode; leading?: React.ReactNode; trailing?: React.ReactNode; onClick?: (e: React.MouseEvent) => void; href?: string; current?: boolean; disabled?: boolean; selectLabel?: string; className?: string }
export declare function ListItem(props: ListItemProps): JSX.Element;
export interface ListSectionProps { title: React.ReactNode; count?: number; note?: React.ReactNode; sticky?: boolean; headingLevel?: 2 | 3 | 4 | 5; children?: React.ReactNode }
export declare function ListSection(props: ListSectionProps): JSX.Element;
export declare function ListSectionHeader(props: ListSectionProps & { id?: string; className?: string }): JSX.Element;
export interface ExpansionEditorProps { title: React.ReactNode; summary?: React.ReactNode; children?: React.ReactNode; onSave?: () => boolean | Promise<boolean | void> | void; onCancel?: () => void; dirty?: boolean; open?: boolean; defaultOpen?: boolean; onOpenChange?: (open: boolean) => void; readOnly?: boolean; readOnlyReason?: string; saveLabel?: string; savedMessage?: string; headingLevel?: 2 | 3 | 4; className?: string }
export declare function ExpansionEditor(props: ExpansionEditorProps): JSX.Element;
export interface FlowStep { id: string; title: string; optional?: boolean; editable?: boolean; description?: string }
export interface StepFlowProps { steps: FlowStep[]; active: string; completed?: string[]; errors?: string[]; mode?: 'linear' | 'nonlinear'; onStepChange?: (id: string) => void; onBack?: () => void; onNext?: () => void; onFinish?: () => void; nextLabel?: string; backLabel?: string; finishLabel?: string; busy?: boolean; label?: string; /** 外から決める id（見出しは `${id}-heading`）。省くと自動で振る / optional id */ id?: string; className?: string; children?: React.ReactNode }
export declare function StepFlow(props: StepFlowProps): JSX.Element;
export interface BottomSheetProps { title: string; open?: boolean; onClose?: () => void; variant?: 'modal' | 'persistent'; actions?: React.ReactNode; expandable?: boolean; defaultCollapsed?: boolean; className?: string; children?: React.ReactNode }
export declare function BottomSheet(props: BottomSheetProps): JSX.Element;
export interface ImageGridItem { id: string | number; src?: string; alt: string; caption?: string; meta?: string }
export interface ImageGridProps { items: ImageGridItem[]; label?: string; onOpen?: (item: ImageGridItem) => void; selectable?: boolean; selected?: (string | number)[]; onSelectionChange?: (ids: (string | number)[]) => void; minTileWidth?: number; aspectRatio?: string; className?: string }
export declare function ImageGrid(props: ImageGridProps): JSX.Element;

/** 分類の模様（KM1-COL-001）。分類は色 × 模様で区別する / Category patterns: categories are color × pattern */
export type CategoryPattern = 'solid' | 'horizontal' | 'vertical' | 'diagonal' | 'grid' | 'crosshatch' | 'dots' | 'checker';
export declare const PATTERNS: CategoryPattern[];
/** i 番目の分類の既定の色と模様 / default color and pattern for the i-th category */
export declare function categoryStyle(index: number): { color: string; pattern: CategoryPattern };
export interface CategoryMarkProps { /** cat-* の名前 */ color?: string; pattern?: CategoryPattern; size?: 'sm' | 'md'; /** 単独で意味を持つときだけ。横に分類名の文字があるなら付けない / only when the mark stands alone */ label?: string; className?: string }
export declare function CategoryMark(props: CategoryMarkProps): JSX.Element;
export interface CategoryLegendItem { label: string; color?: string; pattern?: CategoryPattern }
export interface CategoryLegendProps { items: CategoryLegendItem[]; label?: string; vertical?: boolean; size?: 'sm' | 'md'; className?: string }
export declare function CategoryLegend(props: CategoryLegendProps): JSX.Element;

/** KM1 のアイコンの名前（KM1-ICO-001）/ KM1 icon names */
/** 'calendar-empty' は 'calendar' の別名（非推奨）/ 'calendar-empty' is a deprecated alias of 'calendar' */
export type IconName = 'timetable' | 'add' | 'subtract' | 'dismiss' | 'check' | 'chevron-down' | 'chevron-up' | 'chevron-left' | 'chevron-right' | 'arrow-up' | 'arrow-down' | 'arrow-left' | 'arrow-right' | 'sort' | 'sort-up' | 'sort-down' | 'edit' | 'delete' | 'copy' | 'search' | 'filter' | 'settings' | 'more' | 'more-vertical' | 'drag' | 'menu' | 'home' | 'open-external' | 'link' | 'share' | 'save' | 'download' | 'upload' | 'document' | 'folder' | 'image' | 'tag' | 'person' | 'people' | 'mail' | 'chat' | 'notification' | 'star' | 'eye' | 'eye-off' | 'lock' | 'help' | 'warning' | 'calendar' | 'clock' | 'flag' | 'location' | 'offline' | 'sync' | 'undo' | 'history' | 'print' | 'pin' | 'briefcase' | 'deadline' | 'due-today' | 'tentative' | 'canceled' | 'repeat-weekly' | 'view-day' | 'view-week' | 'view-agenda' | 'shift-work' | 'room-change' | 'submit' | 'exam' | 'status-info' | 'status-success' | 'status-warning' | 'status-error' | 'density-compact' | 'density-regular' | 'density-spacious' | 'cart' | 'receipt' | 'store' | 'product' | 'discount' | 'money' | 'wallet' | 'payment-card' | 'qr-code' | 'ticket' | 'waiting' | 'calculator' | 'barcode-scan' | 'calendar-add' | 'reminder' | 'note' | 'attach' | 'send' | 'phone' | 'globe' | 'camera' | 'person-add' | 'sign-out' | 'sign-in' | 'refresh' | 'list' | 'grid' | 'table' | 'chart' | 'bookmark' | 'heart' | 'cloud' | 'wifi' | 'light-mode' | 'dark-mode' | 'keyboard' | 'zoom-in' | 'zoom-out' | 'expand' | 'collapse' | 'play' | 'pause' | 'mic' | 'volume' | 'map' | 'building' | 'school' | 'book' | 'redo' | 'paste' | 'select-all' | 'key' | 'shield' | 'folder-open' | 'archive' | 'contact-card' | 'bus' | 'weather' | 'task-list' | 'notification-off' | 'lock-open' | 'timer' | 'sparkle' | 'view-month' | 'text-size' | 'filter-dismiss' | 'calendar-empty';
export interface IconProps { name: IconName; /** 'fluent' で導入前の形（比べるとき）/ show the previous Fluent shape */ variant?: 'km1' | 'fluent'; /** 16・20（標準）・24。32 は 24 の形を拡大 / 32 enlarges the 24 drawing */ size?: 16 | 20 | 24 | 32; filled?: boolean; /** 単独で意味を持つときだけ。ボタンの中なら付けない / only when the icon stands alone */ label?: string; className?: string }
export declare function Icon(props: IconProps): JSX.Element;
/** 名前と日本語の名前の一覧 / names with Japanese labels */
export declare const ICONS: Record<IconName, string>;

/** KM1 B 案のアイコンを全体で切り替える（'fluent' で元に戻す）/ switch KM1 B icons app-wide */
export declare function setIconStyle(style: 'km1' | 'fluent'): void;
